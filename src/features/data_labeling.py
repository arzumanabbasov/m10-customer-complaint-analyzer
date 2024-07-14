import os
import json
import logging
import pandas as pd
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from plyer import notification


# Initialize logging
logging.basicConfig(filename='labeling.log', level=logging.INFO)

# Load environment variables
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')

# Initialize Mistral client
client = MistralClient(api_key=MISTRAL_API_KEY)

model = "mistral-large-latest"

# Load dataset
df = pd.read_json(os.path.join(parent_dir, 'data/processed/cleaned_comments_instagram.json'))

# Define categories of pain
pain_categories = [
    "security concerns",
    "user experience issues",
    "regulatory compliance",
    "technical glitches",
    "transaction delays",
    "cost of services",
    "limited functionality",
    "customer support issues",
    "integration challenges",
    "data privacy concerns",
    "cashback problems"
]

# Function to label comments based on the chat model response
def label_comment(dataframe: pd.DataFrame):
    for i, comment in enumerate(dataframe['text']):
        messages = [
            ChatMessage(
                role="user",
                content=f"You will get comment from instagram page of digital wallet app in Azerbaijan. Comments are in Azerbaijani language, identify if the customer is having a pain, if haves what type of pain it is. Comments in Azerbaijani and try your best. If it is a pain, identify the category. Return the information in a short JSON object with 2 values is_pain:boolean and pain_type, if is_pain is false then pain_type is None.\n\nComment:\n{comment}\n\nPain Categories: {', '.join(pain_categories)}"
            )
        ]
        chat_response = client.chat(
            model=model,
            response_format={"type": "json_object"},
            messages=messages,
        )
        response_content = chat_response.choices[0].message.content
        response_json = json.loads(response_content)

        print(i, end="\t")
        print(comment)
        print(response_content)
        print("===== ===== =====")

        try:
            with open('second_labeling.txt', 'a') as file:
                if response_json['is_pain']:
                    file.write(f"{i}\tpain_point\t{response_json['pain_type']}\n")
                else:
                    file.write(f"{i}\telse\tNone\n")
        except:
            file.write(f"{i}\texception happened\tNone\n")
            break


if __name__ == "__main__":
    label_comment(df.iloc[1200:1300, :])
    notification.notify(
        title='Process Finished',
        message="The process finished",
        timeout=20,
        )
    