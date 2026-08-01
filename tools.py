import urllib

from langchain_core.tools import tool
import warnings
import requests
import json

#returns the track id from a search query, the agent will use this in order to retrieve the track id from a user query
@tool
def search_track(Query: str):
    """This allows you to search for information regarding a certain track/album that the user has asked for, the data is returned in the format;
    {'albums': {'href': 'https://api.spotify.com/v1/search?offset=0&limit=5&query=remaster%2520track%3APorcelin%2520artist%3AMobey&type=album', 'limit': 5, 'next': None, 'offset': 0, 'previous': None, 'total': 5, 'items': [{'album_type': 'single', 'total_tracks': 12, 'external_urls': {'spotify': 'https://open.spotify.com/album/79ibiw2nOOcNiCt0XdkwLI'}, 'href': 'https://api.spotify.com/v1/albums/79ibiw2nOOcNiCt0XdkwLI', 'id': '79ibiw2nOOcNiCt0XdkwLI', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273ebe8aa749bd85d8b839b8051', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02ebe8aa749bd85d8b839b8051', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851ebe8aa749bd85d8b839b8051', 'width': 64}], 'name': 'Porcelain', 'release_date': '2000-04-25', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:79ibiw2nOOcNiCt0XdkwLI', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3OsRAKCvk37zwYcnzRf5XF'}, 'href': 'https://api.spotify.com/v1/artists/3OsRAKCvk37zwYcnzRf5XF', 'id': '3OsRAKCvk37zwYcnzRf5XF', 'name': 'Moby', 'type': 'artist', 'uri': 'spotify:artist:3OsRAKCvk37zwYcnzRf5XF'}]}, {'album_type': 'album', 'total_tracks': 18, 'external_urls': {'spotify': 'https://open.spotify.com/album/4KZWx8zo5ym89aopr0dBIb'}, 'href': 'https://api.spotify.com/v1/albums/4KZWx8zo5ym89aopr0dBIb', 'id': '4KZWx8zo5ym89aopr0dBIb', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273f675ddc7a8c113362f983f8b', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02f675ddc7a8c113362f983f8b', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851f675ddc7a8c113362f983f8b', 'width': 64}], 'name': 'Play', 'release_date': '1999-05-17', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:4KZWx8zo5ym89aopr0dBIb', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3OsRAKCvk37zwYcnzRf5XF'}, 'href': 'https://api.spotify.com/v1/artists/3OsRAKCvk37zwYcnzRf5XF', 'id': '3OsRAKCvk37zwYcnzRf5XF', 'name': 'Moby', 'type': 'artist', 'uri': 'spotify:artist:3OsRAKCvk37zwYcnzRf5XF'}]}, {'album_type': 'album', 'total_tracks': 18, 'external_urls': {'spotify': 'https://open.spotify.com/album/200xhXQBPc2OWPsZ3koxTc'}, 'href': 'https://api.spotify.com/v1/albums/200xhXQBPc2OWPsZ3koxTc', 'id': '200xhXQBPc2OWPsZ3koxTc', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273c6c3ea4f348b73b7f8a20bd4', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02c6c3ea4f348b73b7f8a20bd4', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851c6c3ea4f348b73b7f8a20bd4', 'width': 64}], 'name': '18', 'release_date': '2002-05-13', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:200xhXQBPc2OWPsZ3koxTc', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3OsRAKCvk37zwYcnzRf5XF'}, 'href': 'https://api.spotify.com/v1/artists/3OsRAKCvk37zwYcnzRf5XF', 'id': '3OsRAKCvk37zwYcnzRf5XF', 'name': 'Moby', 'type': 'artist', 'uri': 'spotify:artist:3OsRAKCvk37zwYcnzRf5XF'}]}, {'album_type': 'album', 'total_tracks': 34, 'external_urls': {'spotify': 'https://open.spotify.com/album/6vcm3ltupPkA4zt82auiKh'}, 'href': 'https://api.spotify.com/v1/albums/6vcm3ltupPkA4zt82auiKh', 'id': '6vcm3ltupPkA4zt82auiKh', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2738211d82646eba36b26907b9a', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e028211d82646eba36b26907b9a', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048518211d82646eba36b26907b9a', 'width': 64}], 'name': 'Play: The Complete Recordings', 'release_date': '1999-05-17', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:6vcm3ltupPkA4zt82auiKh', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3OsRAKCvk37zwYcnzRf5XF'}, 'href': 'https://api.spotify.com/v1/artists/3OsRAKCvk37zwYcnzRf5XF', 'id': '3OsRAKCvk37zwYcnzRf5XF', 'name': 'Moby', 'type': 'artist', 'uri': 'spotify:artist:3OsRAKCvk37zwYcnzRf5XF'}]}, {'album_type': 'album', 'total_tracks': 12, 'external_urls': {'spotify': 'https://open.spotify.com/album/4PNGCsIJUFlEoDFhzcu9Il'}, 'href': 'https://api.spotify.com/v1/albums/4PNGCsIJUFlEoDFhzcu9Il', 'id': '4PNGCsIJUFlEoDFhzcu9Il', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b27351d999a5abe49d96ffd7280b', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e0251d999a5abe49d96ffd7280b', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d0000485151d999a5abe49d96ffd7280b', 'width': 64}], 'name': 'Moseley Shoals', 'release_date': '1996-01-01', 'release_date_precision': 'day', 'type': 'album', 'uri': 'spotify:album:4PNGCsIJUFlEoDFhzcu9Il', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/5vIOGcdmx1eIkq3ZtuS12U'}, 'href': 'https://api.spotify.com/v1/artists/5vIOGcdmx1eIkq3ZtuS12U', 'id': '5vIOGcdmx1eIkq3ZtuS12U', 'name': 'Ocean Colour Scene', 'type': 'artist', 'uri': 'spotify:artist:5vIOGcdmx1eIkq3ZtuS12U'}]}]}}
    In order to search for a track you must write it as a query string for example the song above was searched using q=remaster%2520track%3APorcelin%2520artist%3AMobey&type=track, with this trying to search for the song Porcelin by Moby
    """
    try:
        #retrieves the current access token
        with open("json.spotify_tokens", "r") as file:
            data = json.load(file)
            access_token = data["access_token"]

        url = 'https://api.spotify.com/v1/search?' + Query
        response = requests.get(url, headers={"Authorization": f"Bearer {access_token}"})
        return response.json()
    except Exception as e:
        return f"Error: {e}"

def get_current_track():
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        access_token = data["access_token"]
    print(access_token)
    response = requests.get("https://api.spotify.com/v1/me/player", headers={"Authorization": f"Bearer {access_token}"})
    print(response.json())

#play a song from a given
@tool
def play_song(Query: str):
    """This allows you to play a given track, it requires that you have the track id, use the tool search_track with the name of the track in order to get the correct track id
    example Query: '6y20BV5L33R8YXM0YuI38N' being the track id"""
    try:
        #retrieve the current access token
        with open("json.spotify_tokens", "r") as file:
            data = json.load(file)
            access_token = data["access_token"]
        track_id = Query
        url = "https://api.spotify.com/v1/me/player/play?"
        body = {"uris": [f"spotify:track:{track_id}"]}
        response = requests.put(url, headers={"Authorization": f"Bearer {access_token}"}, json=body)
        print(response.json())
    except Exception as e:
        return f"Error: {e}"

@tool
def pause_song(Query: str):
    """This allows you to pause the current song playing"""
    try:
        with open("json.spotify_tokens", "r") as file:
            data = json.load(file)
            access_token = data["access_token"]
        url = "https://api.spotify.com/v1/me/player/pause"
        requests.put(url, headers={"Authorization": f"Bearer {access_token}"})
    except Exception as e:
        return f"Error: {e}"

@tool
def resume_song(Query: str):
    """This allows you to resume the current song, requires the """
    try:
        with open("json.spotify_tokens", "r") as file:
            data = json.load(file)
            access_token = data["access_token"]
        url = "https://api.spotify.com/v1/me/player/play"
        requests.put(url, headers={"Authorization": f"Bearer {access_token}"})
    except Exception as e:
        return f"Error: {e}"

def play_song_test():
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        access_token = data["access_token"]

def get_avaliable_devices():
    try:
        with open("json.spotify_tokens", "r") as file:
            data = json.load(file)
            access_token = data["access_token"]
        url = "https://api.spotify.com/v1/me/player/devices"
        requests.put(url, headers={"Authorization": f"Bearer {access_token}"})
    except Exception as e:
        return f"Error: {e}"

tools = [search_track, play_song, pause_song, resume_song]

"""
def get_current_track():
    with open("json.spotify_tokens", "r") as file:
        data = json.load(file)
        access_token = data["access_token"]
    print(access_token)
    response = requests.get("https://api.spotify.com/v1/me/player", headers={"Authorization": f"Bearer {access_token}"})
    print(response.json())
"""