import os
import json
import pandas as pd
from dotenv import load_dotenv
import logging
import numpy as np

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define paths
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
dataset_path = os.path.join(parent_dir, 'labeled_m10.xlsx')

dataframe = pd.read_excel(dataset_path)


print(dataframe.shape)
dataframe = dataframe[dataframe['pain_type'] != ""]
print(dataframe.shape)

print("=====")
print(dataframe['pain_type'].value_counts())