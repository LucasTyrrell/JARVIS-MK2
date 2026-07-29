import base64
import os

import requests
from dotenv import load_dotenv
import json

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

#response = requests.post(url, params={"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI}, headers=headers)

def refresh_tokens():
    #reading the previouse refresh token from the json file
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        refresh_token = data["refresh_token"]
    #send the post request to recieve the new access and refresh tokens
    response = requests.post(url, params={"grant_type": "refresh_token", "refresh_token": refresh_token}, headers=headers)
    json_data = response.json()
    print(response)
    new_access_token = response.json()["access_token"]
    print(new_access_token)
    #sometimes it doesnt return a new refresh token
    if json_data.get("refresh_token"):
        #if so store the new one
        new_refresh_token = response.json()["refresh_token"]
        with open("json.spotify_tokens", "w") as file:
            json.dump({"access_token": new_access_token, "refresh_token": new_refresh_token}, file)
    else:
        #otherwise just keep the old one
        print(new_access_token)
        with open("json.spotify_tokens", "w") as file:
            json.dump({"access_token": new_access_token, "refresh_token": refresh_token}, file)




refresh_tokens()