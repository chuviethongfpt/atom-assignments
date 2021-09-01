import pandas as pd
import numpy as np
import streamlit as st
import json
import os
from google.cloud import bigquery

# Define credentials 
client = bigquery.Client(credentials=credentials)


#Streamlit app
st.set_page_config(layout="wide")
st.title("Handpick Files")

#Function
def file_selector(folder_path='.', target="background"):
    filenames = [f for f in os.listdir(folder_path) if
                 not f[0] == "."]  # get file names from dir excluding hidden files
    selected_filename = st.selectbox(f'Select a {target}', filenames)
    abs_path = os.path.join(folder_path, selected_filename)
    if os.path.isdir(abs_path):
        return file_selector(abs_path, target)
    return os.path.join(folder_path, selected_filename)

#Setup file upload
uploaded_file = st.file_uploader(label="Import Master Data Here.")

global df
if uploaded_file is not None:
    try:
        df= pd.read_excel(uploaded_file)
    except Exception as e:
        print(e)
        df= pd.read_csv(uploaded_file)
try:
    st.write(df)
except Exception as e:
    print(e)
    st.write("Please upload an Excel file")

