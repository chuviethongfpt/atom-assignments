import pandas as pd
import numpy as np
import streamlit as st
#from google.oauth2 import service_account
#from google.cloud import bigquery

import streamlit.components.v1 as stc

# Create API client.
#credentials = service_account.Credentials.from_service_account_info(
  # st.secrets["service_account"]
#)
#client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.

st.set_page_config(layout="wide")

st.title("Handpick Files")
input = st.file_uploader("Upload An Excel File")

#Setup file upload
uploaded_file = st.sidebar.file_uploader(label="Upload An Excel File. (200MB)", type=['csv','xlxs'])
global df
if uploaded_file is not None:
    print('Upload_file')

    try:
        df= pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df= pd.read_excel(uploaded_file)
try:
    st.write(df)
except Exception as e:
    print(e)
    st.write("Please upload file to the application")
