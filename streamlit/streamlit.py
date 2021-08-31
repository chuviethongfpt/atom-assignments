import pandas as pd
import numpy as np
import streamlit as st
#from google.oauth2 import service_account
#from google.cloud import bigquery

import streamlit.components.v1 as stc

#Create API client.
#credentials = service_account.Credentials.from_service_account_info(
  #st.secrets[""]
#)
#client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
#def run_query(query):
   # query_job = client.query(query)
   # rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache to hash the return value.
    #rows = [dict(row) for row in rows_raw]
   # return rows

#rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# Uses st.cache to only rerun when the query changes or after 10 min.

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
    st.write("File Upload show here")
