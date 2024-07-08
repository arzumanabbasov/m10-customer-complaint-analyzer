import os
import json
import pandas as pd
from dotenv import load_env
from dotenv import load_dotenv
from text_cleaners import TextCleaner

logging.basicConfig(filename='modelling.log', level=logging.INFO)

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
data_path = os.path.join(parent_dir, 
	'data/processed/cleaned_comments_instagram.json')
labels_path = os.path.join(parent_dir, 'data/external/labels.txt')

labels = pd.read_csv(labels_path, delimiter='\t')
data = pd.read_json(data_path)

dataset = data.merge(labels, left_on='index')

