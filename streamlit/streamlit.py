import streamlit as st
import numpy as np
from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account
from google.cloud import bigquery

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

#Streamlit app
st.set_page_config(layout="wide")
st.title("Handpick Files")

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

#Bigquery
