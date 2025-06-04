import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Ethereum Scam Transaction Dashboard",
    layout="wide"
)

# Load your data
@st.cache_data
def load_data():
    return pd.read_csv("../Data/Features/feature_ethereum_data_with_ratios.csv")

df = load_data()

# --- Data Preparation ---
df['total_value'] = df['total_ether_sent'] + df['total_ether_received']
df['tx_count'] = df['sent_tnx'] + df['received_tnx']
df['avg_tx_size'] = np.where(df['sent_tnx'] > 0, df['total_ether_sent'] / df['sent_tnx'], np.nan)
df['sent_ratio'] = df['sent_tnx'] / (df['sent_tnx'] + df['received_tnx'] + 1e-5)

# --- Sidebar Filters ---
st.sidebar.header("Filter Transactions")
min_value = float(df['total_value'].min())
max_value = float(df['total_value'].max())
value_range = st.sidebar.slider(
    'Total Transaction Value (ETH)', min_value, max_value, (min_value, max_value)
)
scam_only = st.sidebar.checkbox("Show only scam addresses", value=False)

# Apply filters
filtered_df = df[
    (df['total_value'] >= value_range[0]) &
    (df['total_value'] <= value_range[1])
]
if scam_only:
    filtered_df = filtered_df[filtered_df['flag'] == 1]

# --- KPI Metrics ---
st.title("Ethereum Scam Transaction Analysis")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Unique Addresses", filtered_df['address'].nunique())
col2.metric("Scam Addresses", int(filtered_df['flag'].sum()))
col3.metric("Scam %", f"{filtered_df['flag'].mean() * 100:.2f}%" if len(filtered_df) else "0.00%")
col4.metric("Total Transactions", int(filtered_df['tx_count'].sum()))

st.markdown("---")

# --- Median Table for Scam vs Non-Scam ---
st.subheader("Median Values: Scam vs. Non-Scam")
median_table = filtered_df.groupby('flag')[['avg_tx_size', 'tx_count', 'total_ether_sent']].median().rename(
    index={0: "Non-Scam", 1: "Scam"}
)
st.dataframe(median_table.style.format("{:.2f}"), use_container_width=True)

# --- Distribution of Average Transaction Size by Scam Flag (Log Scale) ---
st.subheader("Sent Ratio vs. Average Transaction Size")
fig = px.scatter(
    df,
    x='sent_ratio',
    y='avg_tx_size',
    color=df['flag'].map({0: 'Non-Scam', 1: 'Scam'}),
    color_discrete_map={'Scam': '#354f52', 'Non-Scam': '#84a98c'},
    labels={'color': 'Address Type', 'sent_ratio': 'Sent Ratio', 'avg_tx_size': 'Average TX Size'}
)
fig.update_layout(
    xaxis_title='Sent Ratio',
    yaxis_title='Average Transaction Size (ETH)',
    legend_title='Address Type'
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- User Segmentation Pie Chart ---
st.subheader("User Segmentation: Sender/Receiver/Both")
senders = set(df[df['sent_tnx'] > 0]['address'])
receivers = set(df[df['received_tnx'] > 0]['address'])
sender_only = senders - receivers
receiver_only = receivers - senders
both = senders & receivers
segmentation = {
    'Sender Only': len(sender_only),
    'Receiver Only': len(receiver_only),
    'Both': len(both)
}
seg_df = pd.DataFrame(list(segmentation.items()), columns=["Type", "Count"])
fig_seg = px.pie(
    seg_df, 
    values="Count", 
    names="Type",
    color="Type",
    color_discrete_map={
        "Sender Only": "#52796f",
        "Receiver Only": "#84a98c",
        "Both": "#354f52"
    },
    hole=0.5
)
fig_seg.update_traces(textinfo='percent+label')
st.plotly_chart(fig_seg, use_container_width=True)

st.markdown("---")

# --- Sent Ratio Boxplot ---
st.subheader("Sent Ratio by Scam Flag")
box_df = filtered_df[filtered_df['sent_ratio'].notna() & filtered_df['flag'].notna()]
fig_box = px.box(
    box_df, 
    x=box_df["flag"].map({0: "Non-Scam", 1: "Scam"}),
    y="sent_ratio",
    color=box_df["flag"].map({0: "Non-Scam", 1: "Scam"}),
    color_discrete_map={"Scam": "#354f52", "Non-Scam": "#84a98c"},
    points="all",
    labels={"x": "Address Type", "sent_ratio": "Sent Ratio"},
    title=None
)
fig_box.update_layout(showlegend=False)
st.plotly_chart(fig_box, use_container_width=True)

st.markdown("---")

# --- Pie Chart: Scam vs Non-Scam Addresses ---
st.subheader("Scam vs. Non-Scam Addresses")
scam_counts = filtered_df['flag'].value_counts().rename({0: 'Non-Scam', 1: 'Scam'})
fig_pie = px.pie(
    names=scam_counts.index,
    values=scam_counts.values,
    hole=0.5,
    color=scam_counts.index,
    color_discrete_map={'Scam': '#354f52', 'Non-Scam': '#84a98c'},
    title="Scam vs. Non-Scam Addresses"
)
fig_pie.update_traces(textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")

# --- Top Addresses by Total Value ---
st.subheader("Top 10 Addresses by Total Transaction Value")
top_addresses = (
    filtered_df.groupby('address')['total_value']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
st.dataframe(top_addresses, hide_index=True, use_container_width=True)

st.markdown("---")
st.caption("Data source: Your Ethereum dataset | Dashboard by [Your Name]")