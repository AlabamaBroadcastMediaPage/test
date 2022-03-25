//ha cmdben írod
//cd parancsal keresd meg a mappát
// aztán streamlit run filenév
//ha xml not find hibát kapsz akkor pip install lxml
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('News Explorer')

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

# Web scraping of NBA player stats
@st.cache
def load_data(year):
    url = 
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    #newsdatas = raw.drop(['Rk'], axis=1)
    return playerstats
newsdatas = load_data(selected_year)

# Sidebar - Website selection
sorted_site = sorted(newsdatas.site.unique())
selected_site = st.sidebar.multiselect('Site', sorted_site, sorted_site)

# Sidebar - Title selection
unique_title = sorted(newsdatas.title.unique())
selected_title = st.sidebar.multiselect('title', unique_title, unique_title)

# Filtering data
df_selected_site = newsdatas[(newsdatas.site.isin(selected_site)) & (newsdatas.title.isin(selected_title))]

st.header('Display News of Selected Sites(s)')
st.write('Data Dimension: ' + str(df_selected_site.shape[0]) + ' rows and ' + str(df_selected_site.shape[1]) + ' columns.')
st.dataframe(df_selected_site)
