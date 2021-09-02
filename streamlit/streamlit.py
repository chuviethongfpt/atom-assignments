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

#BigQuery
sql="SELECT * FROM customer.df1"
df1 = pandas_gbq.read_gbq(sql, project_id="handpick-datawarehouse-hdw", credentials=credentials)
project_id="handpick-datawarehouse-hdw"


# #data_frame1,2,3


table_id = uploaded_file

pandas_gbq.to_gbq(df1, table_id, project_id=project_id)
