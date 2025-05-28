from dotenv import load_dotenv
import os
import sys

load_dotenv(dotenv_path="notebooks/.env") 
api_key = os.environ.get("ETHERSCAN_API_KEY")

if not api_key:
    sys.exit("Error: ETHERSCAN_API_KEY not found. Please check your .env file.")

print("Etherscan API key loaded successfully.")