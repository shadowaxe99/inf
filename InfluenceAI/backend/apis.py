```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# API keys
API_KEYS = os.getenv("API_KEYS")

# Social Media APIs
TWITTER_API = "https://api.twitter.com/1.1"
INSTAGRAM_API = "https://graph.instagram.com"
YOUTUBE_API = "https://www.googleapis.com/youtube/v3"

# Calendar APIs
GOOGLE_CALENDAR_API = "https://www.googleapis.com/calendar/v3"
OUTLOOK_API = "https://graph.microsoft.com/v1.0/me/calendar"

# Payment APIs
STRIPE_API = "https://api.stripe.com/v1"
PAYPAL_API = "https://api.paypal.com/v1"

# Signature APIs
DOCUSIGN_API = "https://account-d.docusign.com/oauth/token"
ADOBE_SIGN_API = "https://api.echosign.com/oauth/token"

# VoIP API
VOIP_API = "https://api.voip.ms"

def get_social_media_data(api, endpoint, params):
    headers = {"Authorization": f"Bearer {API_KEYS[api]}"}
    response = requests.get(f"{globals()[api.upper() + '_API']}/{endpoint}", headers=headers, params=params)
    return response.json()

def post_calendar_event(api, endpoint, data):
    headers = {"Authorization": f"Bearer {API_KEYS[api]}"}
    response = requests.post(f"{globals()[api.upper() + '_API']}/{endpoint}", headers=headers, json=data)
    return response.json()

def create_payment(api, endpoint, data):
    headers = {"Authorization": f"Bearer {API_KEYS[api]}"}
    response = requests.post(f"{globals()[api.upper() + '_API']}/{endpoint}", headers=headers, json=data)
    return response.json()

def generate_signature(api, endpoint, data):
    headers = {"Authorization": f"Bearer {API_KEYS[api]}"}
    response = requests.post(f"{globals()[api.upper() + '_API']}/{endpoint}", headers=headers, json=data)
    return response.json()

def make_call(api, endpoint, data):
    headers = {"Authorization": f"Bearer {API_KEYS[api]}"}
    response = requests.post(f"{globals()[api.upper() + '_API']}/{endpoint}", headers=headers, json=data)
    return response.json()
```