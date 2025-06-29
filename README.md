# Analysing Scam Patterns in Ethereum Transactions

![Thumbnail](Images/Ivy%20Kepiro.png)

## Overview
This project explores transaction patterns on the Ethereum blockchain to identify and analyse scam-related behaviours. Using a combination of data analytics techniques and interactive dashboards, highlights distinguishing features between scam and non-scam addresses and provides actionable insights for the crypto community.

The initial goal was to use up-to-date and reliable scam address data via the Etherscan API. However, due to the lack of accessible, recent, and labeled scam address data through public APIs, the project pivoted to using curated Kaggle dataset. 

## Project Structure
```
Ethereum-Scam-Pattern-Analysis/               
├── Data/                          # Raw and processed datasets
│   ├── raw/
│   └── clean/
│   └── features/
├── Dashboard/                     # Interactive Visualisation app
├── Images/                        # Images used
├── Notebooks/                     # Jupyter notebooks for analysis
│   └── etherscan_api_demo.ipynb
│   └── initial_check.ipynb
│   └── feature_engineering.ipynb
│   └── analysis.ipynb
├── Scripts/                       # Python scripts for data collection and processing
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
└── app.py
```

## Objectives
- **Initial Approach: API-Based Data Collection**
  - Fetch ERC-20 transactions for target addresses via the Etherscan API, including safe timestamp conversion to UTC timezone-aware datetime objects.

- **Exploratory Data Analysis**
  - Analyse token transfer volumes, counterparties, and transaction timelines to extract behavioral indicators of suspicious activity.

- **Pattern Identification**
 - Highlight typical scam/fraud features such as high-frequency self-transactions, use of stablecoins (USDT, USDC), and concentrated counterparties.

- **Interactive Visualisation**
 - Provide Streamlit dashboard to visualise patterns and outliers in scam and non-scam transaction data.


## Key Features
- **_Data Cleaning & Exploration_:** Jupyter notebooks for initial data checks and feature engineering.
- **_Interactive Dashboard_:** Streamlit app for visualising scam vs. non-scam transaction patterns.
- **_Custom Visualisations_**: Includes bar charts, histograms, behavioral segmentation, and more.
- **_API Integration_:** Demonstrates fetching live data from the Etherscan API.
- **Wallet Behavioral Analysis:** Detailed examination of wallet interactions revealing suspicious patterns

## Screenshots of the Analysis

Streamlit Interactive Dashboard Snapshot

![Dashboard](Images/dashboard2.png)

<br>

Eliminating Outliers to have a better chart in Jupyter Notebook

![Outliers](Images/outliers.png)

<br>

Checking Wallet Distribution in Jupyter Notebook

![Distribution](Images/distribution.png)

## Tasks 
 * Data Collection (download and validate datasets from Kaggle, pull additional data using Etherscan API, obtain and integrate scam address lists)
 * Data Cleaning & Preparation (in Jupyter Notebook)
 * Exploratory Data Analysis
 * Visualization of Outliers (Jupyter Notebook)
 * Initial Scam/Fraud Detection Logic
 * Reporting & Documentation (using Streamlit Dashboard)

## Challenges & Lessons Learned
**Data Sourcing Difficulties:**
 * Most public scam address lists are outdated and not recently active.
 * Obtaining recent, labeled scam data through APIs proved difficult; APIs often have strict rate limits and can return incomplete data, making large-scale analysis challenging.

**Pivot to Kaggle Datasets:**
 * To address these issues, I adopted curated, labeled, and often more recent scam address datasets from Kaggle.
 * Kaggle datasets provided transaction-level details, were easier to work with offline, and were not subject to API rate limits or data incompleteness.
 * This pivot enabled more robust exploration as the data was more reliable than what could be obtained from public lists or direct API calls.

**Data Quality & Imbalance:**
 * The datasets are highly imbalanced, with far fewer scam transactions than legitimate ones, requiring careful preprocessing and consideration in analysis.
 * Addressed missing values, zeros, and outliers to ensure meaningful feature engineering.

**Visualisation Issues:**
 * Some charts in Streamlit (especially those using log scales or visualising skewed data) were difficult to interpret due to data distribution (many zeros or extreme outliers).
 * Required creative alternatives and filtering to present clear, actionable insights.

**Dependency & Code Management:**
 * Streamlined requirements.txt to include only essential packages, reducing errors and simplifying collaboration.
 * Cleaned up unused imports and dependencies for a smoother workflow.

## Data Sources
- **Kaggle Ethereum Datasets:** For historical transactions and labeled fraud data.
- **Etherscan API:** Used for supplementary live and historical transaction data (where possible).
- **Public Scam Address Lists:** (e.g., EtherScamDB, EthScamCheck) for reference and cross-validation.

*Powered by Etherscan.io APIs and Kaggle datasets.*

## Getting Started
1. Clone this repository:

   ```git clone `https://github.com/InsightsByIvy/Analysing-Scam-Patterns-in-Ethereum-Transactions```

2. Install dependencies:
   Run `pip install -r requirements.txt` to install dependencies.


## Notes

This project is a work in progress and will be updated as new features are added.

Live Demo
👉 View the Streamlit Dashboard [Here](https://analysing-scam-patterns-in-ethereum-transactions.streamlit.app/)

For educational and demonstration purposes only.

[Back to top](#analysing-scam-patterns-in-ethereum-transactions)
