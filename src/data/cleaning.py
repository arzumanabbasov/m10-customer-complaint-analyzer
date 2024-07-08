import os 
import json
import logging
import requests
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from text_cleaners import TextCleaner

logging.basicConfig(filename='data_processing.log', level=logging.INFO)

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(os.path.dirname(current_dir))
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)


RAW_DATA_PATH = os.environ.get("RAW_DATA_PATH")



def load_data(raw_data_path):
    """
    Loads data from a JSON API endpoint and filters unwanted records.
    
    Args:
    - raw_data_path (str): URL endpoint to fetch raw data.
    
    Returns:
    - pd.DataFrame: Cleaned DataFrame containing 'ownerUsername', 'timestamp', 'text' columns.
    """
    try:
        response = requests.get(raw_data_path)
        response.raise_for_status()  # Raise error for bad response status
        data = response.json()
        df = pd.DataFrame(data)
        # Filter out records where 'ownerUsername' is 'm10.az'
        df = df[df['ownerUsername'] != 'm10.az']
        # Filter out records where 'text' length is less than 50 characters
        df = df[df['text'].str.len() >= 50]
        df = df[['ownerUsername', 'timestamp', 'text']]
        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


def clean_data(dataframe):
    """
    Cleans text data in 'text' column of the given DataFrame.
    
    Args:
    - dataframe (pd.DataFrame): DataFrame containing 'text' column to be cleaned.
    
    Returns:
    - pd.DataFrame: DataFrame with cleaned 'text' column.
    """
    try:
        dataframe['text'] = TextCleaner(list(dataframe['text'])).clean_text()
        return dataframe

    except Exception as e:
        print(f"Error cleaning data: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error


if __name__ == "__main__":

    try:
        df = load_data(RAW_DATA_PATH)
        df = clean_data(df)
        df = df.reset_index()
        df.to_json(os.path.join(parent_dir, 'data/processed/cleaned_comments_instagram.json'))
        logging.info("Data cleaning and processing completed successfully.")


    except Exception as e:
        logging.error(f"Error processing data: {str(e)}")
