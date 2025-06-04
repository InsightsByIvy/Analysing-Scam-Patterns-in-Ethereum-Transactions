import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


#Set page configuration
st.set_page_config(
    page_title="Ethereum Scam Transaction Analysis", layout="wide", initial_sidebar_state="expanded")

# Import data
@st.cache_data
def load_data():
    df = pd.read_csv('../Data/Features/feature_ethereum_data_with_ratios.csv')
    return df
df = load_data()
st.write("COLUMNS IN DF:", df.columns.tolist())

# Sidebar
st.sidebar.header("Navigation")
section = st.sidebar.radio("Choose a section", ["Overview", "User Segmentation", "Feature Analysis", "Transaction Analysis", "Scam Detection"])


# Header
st.title("Ethereum Scam Transaction Analysis")

# Overview Section
if section == "Overview":
    st.subheader("Overview Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Unique Addresses", df['address'].nunique())
    col2.metric("Scam Addresses", int(df['flag'].sum()))
    col3.metric("Scam %", f"{df['flag'].mean() * 100:.2f}%")

    st.markdown("""
    - Total ETH sent and received values are already in ETH units.
    - Scam addresses make up approximately 22% of the dataset.
    """)

# User Segmentation Section
elif section == "User Segmentation":
    st.subheader("User Segmentation by Behaviour")
    senders = set(df[df['sent_tnx'] > 0]['address'])
    receivers = set(df[df['received_tnx'] > 0]['address'])

    sender_only = senders - receivers
    receiver_only = receivers - senders
    both = senders & receivers

    labels = ['Sender Only', 'Receiver Only', 'Both']
    sizes = [len(sender_only), len(receiver_only), len(both)]
    pie_chart = px.pie(values=sizes, names=labels, title='Wallet Roles')
    st.plotly_chart(pie_chart)

    # Display unique addresses
    st.write(f"Total Unique Addresses: {df['address'].nunique()}")
    st.write(f"Total Scam Addresses: {int(df['flag'].sum())}")

# Feature Analysis Section
elif section == "Feature Analysis":
    st.subheader("Transaction Patterns")

    tab1, tab2 = st.tabs(["Average Transaction Size", "Transaction Count"])


    with tab1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            data = df[df["avg_tx_size"].notna()],
            x="avg_tx_size",
            hue="flag",
            bins=50,
            log_scale=True,
            ax=ax
        )
        st.pyplot(fig)
