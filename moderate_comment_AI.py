
from openai import AzureOpenAI
import pandas as pd # file management
from profanity_check import predict, predict_prob
from key import API_KEY  # Import the API key 

import nltk # NLP library https://www.nltk.org/
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree
from nltk.tag import pos_tag

import joblib

#download nltk resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('maxent_ne_chunker_tab')

# Set the version, base URL and API key for the OpenAI client
client = AzureOpenAI(
    api_version="2023-03-15-preview",
    azure_endpoint="https://gpt-moderation.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-03-15-preview",
    api_key = API_KEY,
    )

# Function to get a more objective version of the text
def get_objective_text(text):

    completion = client.chat.completions.create(
        model="gpt-35-turbo",  # here the name of the model
        messages=[
            {"role": "system", "content": "You are an assistant that rewrites texts in an objective, professional manner, and ensures the text is concise. Do not include any introductory phrases in your response."},
            {"role": "user", "content": f"Rewrite the following text in an objective and professional manner, keeping the length similar to or shorter than the original. Do not include any introductory phrases in your response:\n\n{text}"}
        ],
        temperature=0.7,
    )
    return completion.choices[0].message.content

# replace names function
def replace_name(text, replace="[name]"):
    if pd.isna(text) or text.strip().lower() == "nan":  # if text is empty or NaN
        return text, False

    words = word_tokenize(text)
    tagged_words = pos_tag(words)

    modified = False

    for word, tag in tagged_words:
        if tag == 'NNP':
            # Replace exact word tagged as NNP
            text = text.replace(word, replace)
            modified = True

    return text, modified  # second parameter is True if was changed

# read the excel file
df = pd.read_excel('NPS_REASON_EXTRACTED.xlsx')

# convert text in strings
df['NPS_REASON'] = df['NPS_REASON'].astype(str)

# new columns
df['NPS_REASON_EDITTED'] = ''
df['COMMENT'] = ''
df['PROFANITY_PROB'] = 0.0

for index, row in df.iterrows(): # go through all the dataframe
    edited_text, is_modified = replace_name(row['NPS_REASON']) # use the function to replace names
    df.at[index, 'NPS_REASON_EDITTED'] = edited_text # put edited text
    comment = ''
    if is_modified:
        comment = 'Name identified'
    profanity_prob = predict_prob([row['NPS_REASON']])[0] # check for profanity probability
    df.at[index, 'PROFANITY_PROB'] = profanity_prob # put profanity probability
    if profanity_prob > 0.09:  # check if profanity probability is greater than 0.09
        if comment:
            comment += ', '
        comment += 'Inappropriate'
        objective_text = get_objective_text(edited_text) #objective version of the text
        df.at[index, 'NPS_REASON_EDITTED'] = objective_text 
    df.at[index, 'COMMENT'] = comment # put comment when modified or profanity detected

# save modified file
df.to_excel('NPS_REASON_PROCESSED.xlsx', index=False) # save file to excel