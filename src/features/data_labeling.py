import os 
import json
import logging
import pandas as pd
from dotenv import load_dotenv


logging.basicConfig(filename='labeling.log', level=logging.INFO)

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)


MISTRAL_API_KEY = os.environ.get('MISTRAL_API_KEY')

print(MISTRAL_API_KEY)