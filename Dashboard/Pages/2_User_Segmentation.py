import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("../Data/Features/feature_ethereum_data_with_ratios.csv")

df = load_data()

st.header("User Segmentation")

# Example: Pie chart of sender/receiver/both (replace 'segmentation' with your actual column)
import plotly.express as px
if 'segmentation' in df.columns:
    seg_counts = df['segmentation'].value_counts()
    fig = px.pie(
        values=seg_counts.values,
        names=seg_counts.index,
        color_discrete_sequence=['#cad2c5', '#84a98c', '#52796f']
    )
    st.plotly_chart(fig)
else:
    st.info("No segmentation column found in data.")
