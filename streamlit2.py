import pandas as pd
import numpy as np
import altair as alt
import PIL as Image
import base64
import seaborn as sns
import streamlit as st
import scipy.stats as stats
import math
import streamlit.components.v1 as components
import streamlit.components.v1 as stc 
import matplotlib.pyplot as plt
import os
import pickle
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import html5lib
from bs4 import BeautifulSoup

st.title('HANDPICK HACKATHON')
st.subheader('The last fight!')

st.markdown("### **🗂️ Order Processed 🗂️** ")

def load_df():
    df = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis1.csv")
    return df
def load_df1():
    df1 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis4.csv")
    return df1
def load_df2():
    df2 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis3.csv")
    return df2
def load_df3():
    df3 = pd.read_csv(r"C:\Users\PC\Desktop\Py4DS\DATACracy-ATOM\SCALA\HACKATHON\Data\basketanalysis2.csv")
    return df3

df = load_df()
sector = df.groupby('antecedent')
# df1 = load_df1()
# sector1 = df1.groupby('antecedent')
# df2 = load_df2()
# sector2 = df2.groupby('antecedent')
# df3 = load_df3()
# sector3 = df3.groupby('antecedent')

#Sidebar
selected_age = st.sidebar.selectbox("📍 Age Range 📍", ["None","18-24", "25-34", "35-44"])
selected_type1= st.sidebar.checkbox("VIP Users")
selected_type2= st.sidebar.checkbox("Free Users")
sorted_sector_unique = sorted(df['antecedent'].unique() )
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[(df['antecedent'].isin(selected_sector)) ]

st.header('Hello')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)


# def output(age, type1, type2):
#   if age == None:
#     return df['antecedent']
#   elif age == ['18 - 24'] and type1:
#     return df1['antecedent']
#   elif age == ['25 - 34'] and type1:
#     return df2['antecedent']
#   else:
#     return df3['antecedent']
# sector = output(selected_age, selected_type1, selected_type2)
# output(selected_age, selected_type1, selected_type2)
