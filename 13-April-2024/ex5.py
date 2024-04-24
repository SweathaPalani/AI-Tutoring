import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set your Spotify API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

# Initialize Spotipy client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: Search for a track
track_name = "Shape of You"
results = sp.search(q=track_name, type='track')

# Print track details
for track in results['tracks']['items']:
    print("Track Name:", track['name'])
    print("Artist:", track['artists'][0]['name'])
    print("Album:", track['album']['name'])
    print("Preview URL:", track['preview_url'])
    print()
