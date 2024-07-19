import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get current and parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))

# Update with your actual file path
file_path = os.path.join(parent_dir, 'labeled_m10-cleaned.xlsx')

# Load DataFrame
df = pd.read_excel(file_path)

# Function to save changes to the Excel file
def save_changes(df, file_path):
    df.to_excel(file_path, index=False)

# Function to display a single sample
def display_sample(index):
    sample = df.iloc[index]
    st.write(f"**Timestamp:** {sample['timestamp']}")
    st.info(f"**Text:** {sample['text']}")

    # Current labels
    st.error(f"**Current Pain Type:** {sample['pain_type']}")

    # Define options for selectbox
    pain_type_options = [None,
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
    "cashback problems",
    "transparency concerns",
    "limon"]

    # Label inputs
    pain_type = st.selectbox('Pain Type:', options=pain_type_options, index=pain_type_options.index(sample['pain_type']) if sample['pain_type'] in pain_type_options else 0)

    # Update the DataFrame with the new labels
    df.at[index, 'pain_type'] = pain_type

    # Save changes to the Excel file
    if st.button('Save Changes'):
        save_changes(df, file_path)
        st.success('Changes saved successfully!')

# Interface for sample selection
st.title("Dataset Label Editor")
sample_index = st.number_input('Sample Index:', min_value=0, max_value=len(df)-1, step=1)

display_sample(sample_index)
