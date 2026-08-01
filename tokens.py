import base64
import os

#to get initial auth code
from urllib.parse import urlencode
import webbrowser

import requests
from dotenv import load_dotenv
import json
from apscheduler.schedulers.background import BackgroundScheduler

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
REDIRECT_URI = os.getenv("REDIRECT_URI")
encoded_credentials = base64.b64encode(credentials.encode()).decode()
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {encoded_credentials}"
}
url = "https://accounts.spotify.com/api/token"

scheduler = BackgroundScheduler()

#to be ran every hour as the spotify access token expires after an hour
@scheduler.scheduled_job("interval", minutes=59)
#use the current refresh token to receive a new access token, and maybe a new refresh token
def refresh_tokens():
    #reading the previouse refresh token from the json file
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        refresh_token = data["refresh_token"]
    #send the post request to recieve the new access and refresh tokens
    response = requests.post(url, params={"grant_type": "refresh_token", "refresh_token": refresh_token}, headers=headers)
    json_data = response.json()
    new_access_token = response.json()["access_token"]
    #sometimes it doesnt return a new refresh token
    if json_data.get("refresh_token"):
        #if so store the new one
        new_refresh_token = response.json()["refresh_token"]
        with open("json.spotify_tokens", "w") as file:
            json.dump({"access_token": new_access_token, "refresh_token": new_refresh_token}, file)
            print("new tokens added")
    else:
        #otherwise just keep the old one
        with open("json.spotify_tokens", "w") as file:
            json.dump({"access_token": new_access_token, "refresh_token": refresh_token}, file)
    print("new tokens added")

scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing playlist-read-private user-read-playback-position user-read-playback-position user-read-recently-played user-library-read"

#code_respose = requests.get("https://accounts.spotify.com/api/authorize", params= {"client_id": CLIENT_ID, "response_type": "code", "redirect_uri": REDIRECT_URI, "scope": scope})

#here in case the refresh token runs out, and you need to manually re-authenticate
def get_initial_access_token():
    code = "AQBS9z43AG3EpF_6B2m_HdnqjJCGLji2UUrOeTvpayL3rbBQc7JspP3g1HqknL2AN9xL4OH7rmMvQS6nFcp0Kq9f5ZNSlvTNFL0kKU9Q15WnH6ago8Szt_EkbCBiNzoCI4k4zZTF30fqvgw4lXx13udTNBPKWOhgzddHOrRzT6nM3f_QenA-2fgMa2dbcuNF3BRZqE-rnMnhQx6gLOmApqsKa-ucI1EpN9P3p3lxskqH9lgdhiGwvgMEcLx6DMyq41EKKpqplu6oMd9XZR9mp7W15HxjOztkykciPYMr5k2qZlupfZmemk0kCZSXZRpyZz2My5nVu00MXhYjN00R4_6K2HuI2Be9hkPKsqkKOzZUwjHDPK0hr1FTRPR2jg3U_VnOo9_pT61_2Gn2TZ7d_Gs8j6RE29cHrEzOdtBcEBNRIGdC6YFrB2Hcw5Zb8k_p8iwtLkIfDP7a-eZXKVM"
    access_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI
        },
        headers=headers
    )
    print(access_response.json())



def get_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": scope
    }
    auth_url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    webbrowser.open(auth_url)

#get_initial_access_token()
#get_auth_url()