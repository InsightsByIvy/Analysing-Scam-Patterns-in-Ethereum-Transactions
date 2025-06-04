import streamlit as st
from st_pages import Page, add_page_title

st.set_page_config(
    page_title="Ethereum Scam Detection Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

add_page_title()

# Define the pages to display in the sidebar
show_pages([
    Page("app.py", "Home", "🏠"),
    Page("pages/overview.py", "Overview", "📊"),
    Page("pages/user_segmentation.py", "User Segmentation", "👥"),
    Page("pages/feature_analysis.py", "Feature Analysis", "🔍"),
    Page("pages/transaction_analysis.py", "Transaction Analysis", "💰"),
    Page("pages/scam_detection.py", "Scam Detection", "🚨"),
])

st.title("Ethereum Scam Detection Dashboard")

st.image("../Images/pexels-anna-nekrashevich-6801648.jpg", width=600)

st.markdown("""
<div style="font-size:20px;">
    <p>Welcome! Use the sidebar to navigate between the sections of the dashboard:</p>
    <ul>
        <li>Overview</li>
        <li>User Segmentation</li>
        <li>Feature Analysis</li>
        <li>Transaction Analysis</li>
        <li>Scam Detection</li>
    </ul>
    <p>Each page is designed to explore different aspects of Ethereum scam patterns.</p>
</div>
""", unsafe_allow_html=True)