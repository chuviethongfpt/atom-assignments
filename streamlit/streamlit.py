import pandas as pd
import numpy as np
import streamlit as st
import os
from google.cloud import bigquery

# Define credentials 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'handpick.json'
client = bigquery.Client()
def _fetch_data_bigquery(query):
    """
      Take SQL query in Standard SQL and returns a Pandas DataFrame of results
      ref: https://cloud.google.com/bigquery/docs/reference/standard-sql/enabling-standard-sql
    """
    return client.query(query, location="US").to_dataframe()

#Streamlit app
st.set_page_config(layout="wide")
st.title("Handpick Files")

#Setup file upload
uploaded_file = st.file_uploader(label="Import Master Data Here.")

#global df
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
