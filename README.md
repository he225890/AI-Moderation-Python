# AI Moderation - Python

## Project Overview

This project automates the moderation of user comments using natural language processing (NLP) techniques. It replaces personal names with generic tags to protect privacy and analyzes comments for profanity or inappropriate language. 

The project uses the GPT-3.5 model to transform inappropriate comments into more objective, professional versions. Future enhancements include identifying positive, negative, and mixed comments to conduct a more advanced sentiment analysis.

## Files Included

- `moderate_comment_AI.py`: The main script that processes comments.
- `requirements.txt`: A list of dependencies required to run the project.
- `NPS_REASON_EXTRACTED.xlsx`: The input file containing comments to be processed.

## Requirements

- Python 3.8 or higher.
- The dependencies listed in the `requirements.txt` file.

## Installation

Follow these steps to install and run the project:

```bash
1. Clone this repository:
   git clone https://SMHS-DH-Applications@dev.azure.com/SMHS-DH-Applications/AI%20Moderation%20-%20Python/_git/AI%20Moderation%20-%20Python
   cd AI%20Moderation%20-%20Python
```

2. Create a virtual environment and install dependencies:
```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
```

3. Before running the program, create a `key.py` file containing your OpenAI API key:
```python
   API_KEY = 'YOUR_API_KEY_HERE'
```

4. Run the main script:
```bash
   python moderate_comment_AI.py
```

   The script will generate an `NPS_REASON_PROCESSED.xlsx` file with the moderated comments after a few minutes of processing.

## How It Works

The project processes comments from an Excel file and performs the following tasks:
- **Name replacement**: Replaces personal names with the `[name]` tag.
- **Profanity detection**: Analyzes each comment for profanity and tags comments with high profanity probability.
- **Text transformation**: If inappropriate language is detected, the comment is rewritten into a more objective and professional version using the GPT-3.5 model.
- **Output**: The processed comments are saved in a new Excel file (`NPS_REASON_PROCESSED.xlsx`).

## Running the Project

After setting up the environment and adding the `key.py` file, you can execute the following commands to run the project:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python moderate_comment_AI.py
```

The script will process the comments and generate the `NPS_REASON_PROCESSED.xlsx` file in the current directory.

## Security Note

The `key.py` file containing the OpenAI API key is **not included** in this repository for security reasons. You must add this file manually before running the program. The key file should have the following format:

```python
API_KEY = 'YOUR_API_KEY_HERE'
```

## Future Work

This project can be extended to:
- Identify positive, negative, and mixed comments to help analyze user sentiment.
- Implement additional features for more advanced content moderation and analysis.

