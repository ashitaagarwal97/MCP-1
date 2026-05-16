import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()

BASE_URL = os.getenv("SALESFORCE_BASE_URL")
CLIENT_ID = os.getenv("SALESFORCE_CLIENT_ID")
CLIENT_SECRET = os.getenv("SALESFORCE_CLIENT_SECRET")
USERNAME = os.getenv("SALESFORCE_USERNAME")
PASSWORD = os.getenv("SALESFORCE_PASSWORD")

access_token = None
instance_url = None

# Salesforce Authentication Method
def authenticate():
    global access_token, instance_url
    auth_url = f"{BASE_URL}/services/oauth2/token"
    response = requests.post(
        auth_url,
        data={
            "grant_type": "password",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "username": USERNAME,
            "password": PASSWORD
        }
    ).json()

    if "access_token" not in response:
        raise Exception(f"Auth failed: {response}")

    access_token = response["access_token"]
    instance_url = response["instance_url"]

def get_access_token():
    authenticate()      # ✅ Always fetch fresh token
    return access_token

def get_instance_url():
    authenticate()      # ✅ Always fetch fresh token
