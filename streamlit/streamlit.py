import streamlit as st
import numpy as np
from google.oauth2 import service_account
import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

#Streamlit app
st.set_page_config(layout="wide")
st.title("Handpick Files")

#checkbox

if st.checkbox("Import Product File"):
    product_file = st.file_uploader(label="Product File is loading...")

    global df1
    if product_file is not None:
        try:
            df1= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df1= pd.read_csv(product_file)
    try:
        st.write(df1)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import Customer File"):
    product_file = st.file_uploader(label="Customer File is loading...")

    global df2
    if product_file is not None:
        try:
            df2= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df2= pd.read_csv(product_file)
    try:
        st.write(df2)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import Inventory File"):
    product_file = st.file_uploader(label="Inventory File is loading...")

    global df3
    if product_file is not None:
        try:
            df3= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df3= pd.read_csv(product_file)
    try:
        st.write(df3)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import Sup_Product File"):
    product_file = st.file_uploader(label="Sub_Product File is loading...")

    global df4
    if product_file is not None:
        try:
            df4= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df4= pd.read_csv(product_file)
    try:
        st.write(df4)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import Production File"):
    product_file = st.file_uploader(label="Production File is loading...")

    global df5
    if product_file is not None:
        try:
            df5= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df5= pd.read_csv(product_file)
    try:
        st.write(df5)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import S.O File"):
    product_file = st.file_uploader(label="S.O File is loading...")

    global df6
    if product_file is not None:
        try:
            df6= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df6= pd.read_csv(product_file)
    try:
        st.write(df6)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import D.O File"):
    product_file = st.file_uploader(label="D.O File is loading...")

    global df7
    if product_file is not None:
        try:
            df7= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df7= pd.read_csv(product_file)
    try:
        st.write(df7)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import G.O File"):
    product_file = st.file_uploader(label="G.O File is loading...")

    global df8
    if product_file is not None:
        try:
            df8= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df8= pd.read_csv(product_file)
    try:
        st.write(df8)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel or CSV file")

if st.checkbox("Import Return S.O File"):
    product_file = st.file_uploader(label="Return S.O File is loading...")

    global df9
    if product_file is not None:
        try:
            df9= pd.read_excel(product_file)
        except Exception as e:
            print(e)
            df9= pd.read_csv(product_file)
    try:
        st.write(df9)
    except Exception as e:
        print(e)
        st.write("Please upload an Excel of CSV file")
        
#Bigquery
