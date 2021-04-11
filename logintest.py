import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
cid = "766b98550bef4a44b8d111658e985c52"
secret = "0e2c82a346254d93bc29e6cfec0ef402"

os.environ["SPOTIPY_CLIENT_ID"] = cid
os.environ["SPOTIPY_CLIENT_SECRET"] = secret
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8080'

username = ""
scope = 'playlist-modify-public playlist-modify-private user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


# client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# token = util.prompt_for_user_token(username, scope)
# if token:
#     sp = spotipy.Spotify(auth=token)
# else:
#     print("Can't get token for", username)