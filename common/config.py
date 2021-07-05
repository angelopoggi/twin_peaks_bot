import os
from dotenv import load_dotenv
try:
    load_dotenv(dotenv_path='.env')
except Exception:
    raise Exception("Cloud not load .env file, please make sure you have one configured")

username = os.environ['username']
password = os.environ['password']
secret = os.environ['client_id']
client = os.environ['client_id']
agent = os.environ['user_angel']
subreddit = os.environ['subreddit']

