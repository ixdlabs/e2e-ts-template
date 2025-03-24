import os
from dotenv import load_dotenv

load_dotenv()


KEYCLOAK_URL = os.environ.get("KEYCLOAK_URL")
REALM = os.environ.get("REALM")
CLIENT_ID = os.environ.get("CLIENT_ID")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
SITE_ID = os.environ.get("SITE_ID")
