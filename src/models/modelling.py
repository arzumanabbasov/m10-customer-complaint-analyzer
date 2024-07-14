import os
import json
import pandas as pd
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define paths
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
labels_path = os.path.join(parent_dir, 'src/features/second_labeling.txt')
dataset_path = os.path.join(parent_dir, 'data/processed/cleaned_comments_instagram.json')

# Load dataset
logger.info("Loading datasets.")
labels = pd.read_csv(labels_path, delimiter='\t')
comments = pd.read_json(dataset_path)

# Check columns of the comments DataFrame
logger.info(f"Columns in comments DataFrame: {comments.columns}")

# Reset index for labels
labels.reset_index(drop=True, inplace=True)

# Select first 1299 rows from comments and drop 'index' column if exists
comments = comments.iloc[:1300, :].drop(columns=['index'], errors='ignore')

# Convert timezone-aware datetime columns to timezone-unaware datetime
for col in comments.select_dtypes(include=['datetimetz']).columns:
    comments[col] = comments[col].dt.tz_localize(None)

# Merge dataframes
dataframe = comments.merge(labels, left_index=True, right_index=True)

# Define output path
output_path = os.path.join(parent_dir, 'labeled_m10.xlsx')

# Write to Excel
logger.info("Writing DataFrame to Excel.")
dataframe.to_excel(output_path, index=False)

logger.info("Finished writing to Excel.")
