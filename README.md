# Analysing Scam Patterns in Ethereum Transactions

## Overview
This project analyses Ethereum blockchain transactions to identify patterns associated with scam or fraudulent activity. The initial goal was to use up-to-date and reliable scam address data via the Etherscan API. However, due to the lack of accessible, recent, and labeled scam address data through public APIs, the project pivoted to using curated Kaggle datasets. This approach enables deeper exploration of transaction behaviors, highlights suspicious addresses, and demonstrates foundational compliance analytics techniques.

## Objectives
- **Initial Approach: API-Based Data Collection**
  - Attempted to gather scam addresses and transaction data using public APIs (e.g., Etherscan).
  - Intended workflow:
    - Fetch scam addresses from blacklists.
    - Check activity and transaction data via API calls.

  **Challenges:**
  - Most public scam address lists are outdated and not recently active.
  - Difficulty obtaining recent, labeled scam data through APIs.
  - API rate limits and incomplete data hindered large-scale analysis.

- **Pivot to Kaggle Datasets**
  - Adopted curated, labeled, and often more recent scam address data from Kaggle.
  - Kaggle datasets include transaction-level details, are easier to work with offline, and are not subject to API rate limits.

- **Analysis Goals**
  - Explore and visualize transaction patterns.
  - Identify features indicative of fraudulent or suspicious activity.
  - Lay the groundwork for future compliance or scam-detection models.

## Data Sources
- **Kaggle Ethereum Datasets:** For historical transactions and labeled fraud data.
- **Etherscan API:** Used for supplementary live and historical transaction data (where possible).
- **Public Scam Address Lists:** (e.g., EtherScamDB, EthScamCheck) for reference and cross-validation.

*Powered by Etherscan.io APIs and Kaggle datasets.*

## Project Structure
```
.
├── data/                # Raw and processed datasets
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/             # Python scripts for data collection and processing
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```
```

## Tasks 
 * Data Collection (Download and validate datasets, Pull additional data using Etherscan API, Obtain and integrate scam address lists)
 * Data Cleaning & Preparation
 * Exploratory Data Analysis (EDA)
 * Visualization of Transaction Patterns
 * Initial Scam/Fraud Detection Logic
 * Reporting & Documentation

## Getting Started
1. Clone this repository:
bash
   ```git clone `https://github.com/InsightsByIvy/Analysing-Scam-Patterns-in-Ethereum-Transactions```

2. Install dependencies:
   Run `pip install -r requirements.txt` to install dependencies.


## Notes
This project is a work in progress and will be updated as new features are added.
For educational and demonstration purposes only.

[Back to top](#Analysing-Scam-Patterns-in-Ethereum-Transactions)
