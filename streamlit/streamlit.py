import streamlit as st
import numpy as np
from google.oauth2 import service_account
import pandas as pd
import pandas_gbq
from googleapiclient.discovery import build
from google.cloud import bigquery
import json
#import mysql.connector
import os
from PIL import Image
import streamlit.components.v1 as components
import streamlit.components.v1 as stc 
import codecs
import sys
from apiclient.discovery import build
#from oauth2client.service_account import ServiceAccountCredentials

# Create API client.
# credentials = service_account.Credentials.from_service_account_info(
#     st.secrets['gcp_service_account']
# )
# client = bigquery.Client(credentials=credentials)
[gcp_service_account]
type = "service_account"
project_id = "hp-data-324704"
private_key_id= "dd1c1b3c55df0fb1aefcef6970339a7992d48f98"
private_key= "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDeT7/M4JBjdv8f\nHL0e/Sgo8aZoEpe12iVL/UJDQH5eWpXv6KE0c/SdAW9FJMTFGBwMoBqul9eZUi+M\nEokuUFB7oZjjKRcPrWk99T/h3L+2C7mb0LkQWxH+RadN3AkwwXaWLfooYrJQfO+F\nWrtFR1/SXYor76oOXwqeHn420UApEu8/FmgSVmiduVppZA37bTzcKiHltN259+pd\nxE+Ocr/rdlWPfgll9AxMWD9YUGNkJ34dRRmkCyGhz7sKdPSwiU2AXTcNDeSdceUC\nrZ6RMtOmsRriodM46Ey48iQiovMO56q4muX0HOxXokdptpiDOF29ANTpXJhgjlR3\niCU/nUgxAgMBAAECggEAR98Jd49sLrPkY+cTH0ch6ibBsSi9ol2drDT67KoXkKKB\nkden8kDApte1ZOmvsbaLLuu95I8TdS50T7kYX4A4nNeQCXSZz4g1G4JDvl3zHsQo\no/61Ldv7c7SKE6pc0EXjdEb19oN9+XaCqx67p3idOnHiPzUSyeWhFaBvFoLM1tn9\nM8Wc/hqcaiDNbQ3fXt3xX8upraD9X2CKJXck/WlWbWBJbf6SlLQRt4cXkYfwyBkt\ncNnnhP+YihbXVu1BMS9G+apZCXxEi57oNRuh7bZyuO6Uwv9iiCcnLbf7O+pCmjfF\noA/prGODdt/Xk+R1SK5GkGwJUTFjopCk6PIe0eTi/wKBgQD9lVbJFfebXuS10hEP\ns9dBjgskEb2YQbvWZ83AmHVKzBw7OYq5/3lScbVkoPE3fmlUKLfgMIl46a0VqtUP\nnUz5PhWgM8LXjzKhdBDQs7K3qJG3t12YvQ2gtbstIafs7JLUeclce2sMkeOcffXy\n70EipiPViLd9M5jNgQA1smHp9wKBgQDgbh36FHY2J91zU3iERdFpvLmFrmGGlA5Q\nmnCir2AbmZU8yS6fafm6JJJljlCjbI4M7rrOvSeQkenaRJUlWvPIhj2HLgAlAsBI\nr5shWg+3w1AdOM8wperh/LAsB5DOPw8tNLFdPtppuhG9/AJcpVDNW9wWpuDqxfaz\nE1LOLGAVFwKBgEWT+lIGYwAQk3SIBQJn+AIWtVvaOklSj/WOWdgkfNpfEsf1S+ko\n/eLvLDRGLKlrV/8thPZQmwfAJiuxyfAU2w/wRwLD8QwwUFYYgJyjEcBu0jy0ZUwJ\nY3nbI1aIy4ioiMkf+W4UtxSl2uwPa7KSjy6wo1htwNrrk1ufr60MGu2VAoGBANMK\nWX//W8XDKPe4hzyC1tBCWoZ9m1HMycU75SzmE08A1hgp6oCXS/ChUVTURbnXa6B3\noQylTJ4ix6+rDEDrTRDEQvlp5VLoSl5PW2Y6ZUtdC2nfMN3DN6M4VYWhu6ZmH+RX\nh21ynDoNcX+giawK/HePqN9YH2pFq51rT1N24QcTAoGBAM38vkwyEDgBPL627x8Z\nYNJzp8lsF4HZmIYyIbVfeYyUkzf30wKrwXklqx5zE4EAYaL+bcaaHCbsiFXJ9PDc\nSrL5dfFFPRAGh8jXMFWCGnYMgv6VCG6NIMjFJDE+Ol9F8rGvexc9POgU3Hy/MSLg\nbqZRyMD1YLTYx7YrZGlsSUzN\n-----END PRIVATE KEY-----\n"
client_email= "datawarehouse@hp-data-324704.iam.gserviceaccount.com"
client_id= "105542999787496052690"
auth_uri= "https://accounts.google.com/o/oauth2/auth"
token_uri= "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url= "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url= "https://www.googleapis.com/robot/v1/metadata/x509/datawarehouse%40hp-data-324704.iam.gserviceaccount.com"
    
my_db.connect(type=st.secrets.db_credentials.service_account, 
              project_id=st.secrets.db_credentials.hp-data-324704, 
              private_key_id=st.secrets.db_credentials.dd1c1b3c55df0fb1aefcef6970339a7992d48f98, 
              client_email=st.secrets.db_credentials.datawarehouse@hp-data-324704.iam.gserviceaccount.com, 
              client_id=st.secrets.db_credentials.105542999787496052690, 
              auth_uri=st.secrets.db_credentials.https://accounts.google.com/o/oauth2/auth, 
              token_uri=st.secrets.db_credentials.https://oauth2.googleapis.com/token, 
              auth_provider_x509_cert_url=st.secrets.db_credentials.https://www.googleapis.com/oauth2/v1/certs, 
              client_x509_cert_url=st.secrets.db_credentials.https://www.googleapis.com/robot/v1/metadata/x509/datawarehouse%40hp-data-324704.iam.gserviceaccount.com, 
              private_key=st.secrets.db_credentials.-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDeT7/M4JBjdv8f\nHL0e/Sgo8aZoEpe12iVL/UJDQH5eWpXv6KE0c/SdAW9FJMTFGBwMoBqul9eZUi+M\nEokuUFB7oZjjKRcPrWk99T/h3L+2C7mb0LkQWxH+RadN3AkwwXaWLfooYrJQfO+F\nWrtFR1/SXYor76oOXwqeHn420UApEu8/FmgSVmiduVppZA37bTzcKiHltN259+pd\nxE+Ocr/rdlWPfgll9AxMWD9YUGNkJ34dRRmkCyGhz7sKdPSwiU2AXTcNDeSdceUC\nrZ6RMtOmsRriodM46Ey48iQiovMO56q4muX0HOxXokdptpiDOF29ANTpXJhgjlR3\niCU/nUgxAgMBAAECggEAR98Jd49sLrPkY+cTH0ch6ibBsSi9ol2drDT67KoXkKKB\nkden8kDApte1ZOmvsbaLLuu95I8TdS50T7kYX4A4nNeQCXSZz4g1G4JDvl3zHsQo\no/61Ldv7c7SKE6pc0EXjdEb19oN9+XaCqx67p3idOnHiPzUSyeWhFaBvFoLM1tn9\nM8Wc/hqcaiDNbQ3fXt3xX8upraD9X2CKJXck/WlWbWBJbf6SlLQRt4cXkYfwyBkt\ncNnnhP+YihbXVu1BMS9G+apZCXxEi57oNRuh7bZyuO6Uwv9iiCcnLbf7O+pCmjfF\noA/prGODdt/Xk+R1SK5GkGwJUTFjopCk6PIe0eTi/wKBgQD9lVbJFfebXuS10hEP\ns9dBjgskEb2YQbvWZ83AmHVKzBw7OYq5/3lScbVkoPE3fmlUKLfgMIl46a0VqtUP\nnUz5PhWgM8LXjzKhdBDQs7K3qJG3t12YvQ2gtbstIafs7JLUeclce2sMkeOcffXy\n70EipiPViLd9M5jNgQA1smHp9wKBgQDgbh36FHY2J91zU3iERdFpvLmFrmGGlA5Q\nmnCir2AbmZU8yS6fafm6JJJljlCjbI4M7rrOvSeQkenaRJUlWvPIhj2HLgAlAsBI\nr5shWg+3w1AdOM8wperh/LAsB5DOPw8tNLFdPtppuhG9/AJcpVDNW9wWpuDqxfaz\nE1LOLGAVFwKBgEWT+lIGYwAQk3SIBQJn+AIWtVvaOklSj/WOWdgkfNpfEsf1S+ko\n/eLvLDRGLKlrV/8thPZQmwfAJiuxyfAU2w/wRwLD8QwwUFYYgJyjEcBu0jy0ZUwJ\nY3nbI1aIy4ioiMkf+W4UtxSl2uwPa7KSjy6wo1htwNrrk1ufr60MGu2VAoGBANMK\nWX//W8XDKPe4hzyC1tBCWoZ9m1HMycU75SzmE08A1hgp6oCXS/ChUVTURbnXa6B3\noQylTJ4ix6+rDEDrTRDEQvlp5VLoSl5PW2Y6ZUtdC2nfMN3DN6M4VYWhu6ZmH+RX\nh21ynDoNcX+giawK/HePqN9YH2pFq51rT1N24QcTAoGBAM38vkwyEDgBPL627x8Z\nYNJzp8lsF4HZmIYyIbVfeYyUkzf30wKrwXklqx5zE4EAYaL+bcaaHCbsiFXJ9PDc\nSrL5dfFFPRAGh8jXMFWCGnYMgv6VCG6NIMjFJDE+Ol9F8rGvexc9POgU3Hy/MSLg\nbqZRyMD1YLTYx7YrZGlsSUzN\n-----END PRIVATE KEY-----\n)
my_db.connect(**st.secrets.db_credentials)
#Streamlit app
st.set_page_config(layout="wide")

st.title('HANDPICK CONCEPT COMPANY LIMITED')
st.subheader('Data Warehouse - Google BigQuery')
#image = Image.open('C:/Users/PC/Pictures/picture 3.png')
#st.image(image, caption= 'Design by HandPickConcept', use_column_width=True)

st.sidebar.header('HOME')
#image = Image.open('C:/Users/PC/Pictures/picture4.jpg')
#st.sidebar.image(image,width=300)
st.sidebar.subheader('About HANDPICK Concept')
st.sidebar.write('**HANDPICK CONCEPT CO.,LTD**')
st.sidebar.write('📌**Address**: S1 The Sun Avenue Tower, 28 Mai Chi Tho, An Phu Ward, Thu Duc, Ho Chi Minh City, Vietnam')
st.sidebar.write('☎️ **Contact**: xxxxxxxxxx')

st.subheader('HANDPICK DATA')

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s

def normalize_db_table_column(df):
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace(r'\n', '_')
    df.columns = df.columns.str.replace(r'[^\w\s]+', '_')
    df.columns = df.columns.str.lower()
    df.columns = df.columns.to_series().apply(remove_accents)

#Setup push BigQuery
def push_exit_table(df, db_table):
    normalize_db_table_column(df)
    print(df)
    credentials = service_account.Credentials.from_service_account_info(
                my_db.connect
    )
    client = bigquery.Client(credentials=credentials)

    project_id="hp-data-324704"

    pandas_gbq.to_gbq(df,f'DWhandpick.{db_table}', project_id=project_id, if_exists='append')

    st.write("Please upload an Excel or CSV file")



#checkbox

if st.checkbox("Import Files"):
    db_table = st.selectbox("📍 Database Table 📍", ["Customer", "DO", "GO", "Inventory", "Product", "Production", "Return_SO", "SO", "Sup_Product"])
    product_file = st.file_uploader(label="📤 Before selecting the file you want to import, please choosing 'Database Table' first 👆...", type = 'xlsx')
    if product_file:
        print('Process: ', product_file, db_table)
        df1= pd.read_excel(product_file, engine = 'openpyxl')
        st.dataframe(df1)
        push_exit_table(df1, db_table)
