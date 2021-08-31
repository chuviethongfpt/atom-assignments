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

st.title("Handpick Files")
input = st.file_uploader("Upload An Excel File")

#Setup file upload
uploaded_file = st.file_uploader(label="Upload A CSV File.")
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
    st.write("Please upload file to the application")
