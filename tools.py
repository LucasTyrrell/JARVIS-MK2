import urllib

from langchain_core.tools import tool
import warnings
import requests
import json
access_token = "BQDK7xHajToAu4-VR6swN1o4qGQ6VLR5r6c2_hNwW7fZ5qjYkmFHq8UsLFbhVaE0y6uwQOy1NTyVIedBBZq8mPyIl8SIG56NGCoiSdbnrCixacY7I-fI26_Df9uXRwVeusl875ELGlhRF8RIcr2Vmrfp_foP74H6nyp_dOEDVN9KpFh0vThQqgonSKWB0Ej_w3cVrB162NZEINB3DfnAVeZKppqSxCTsFVkD2bM9qN-WCrCP9_YKrG9FilDvm_gwawudatn3"

#returns the track id from a search query
def search_track():
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        access_token = data["access_token"]


    url = 'https://api.spotify.com/v1/search?q=remaster%2520track%3APorcelin%2520artist%3AMobey&type=album'
    response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
    print(response.json())
    return response.json()["albums"]["items"][0]["id"]

def get_current_track():
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        access_token = data["access_token"]
    print(access_token)
    response = requests.get("https://api.spotify.com/v1/me/player", headers={"Authorization": f"Bearer {access_token}"})
    print(response.json())


#testing runs
#get_current_track()
print(search_track())