import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyManager:
    REDIRECT_URI = "http://example.com"

    def __init__(self, client_id, client_secret, username):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.songs_URIs = []
        self.playlist_id = None
        self.scope = "playlist-read-private playlist-modify-private playlist-modify-public ugc-image-upload"
        self.sp = self.authorize_spotify()

    def authorize_spotify(self):
        return spotipy.Spotify(
            auth_manager=SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                                      redirect_uri=SpotifyManager.REDIRECT_URI, scope=self.scope,
                                      show_dialog=True, username=self.username)
        )

    def get_songs_uris(self, top_artist_name, top_songs):
        for i in range(len(top_songs)):
            songs_data = self.sp.search(q=f"artist: {top_artist_name}, track: {top_songs[i]}",
                                        type="track", limit=1)
            self.songs_URIs.append(songs_data["tracks"]["items"][0]["uri"])
        return self.songs_URIs

    def create_playlist(self, top_artist_name, amount_of_songs):
        playlist = self.sp.user_playlist_create(user=self.username,
                                                name=f"{top_artist_name} {amount_of_songs} best hits",
                                                public=False)
        self.playlist_id = playlist["id"]

    def add_tracks_to_playlist(self):
        self.sp.playlist_add_items(playlist_id=self.playlist_id, items=self.songs_URIs)
        return True

    def upload_cover_image(self, img_base64):
        try:
            self.sp.playlist_upload_cover_image(playlist_id=self.playlist_id, image_b64=img_base64)
        except spotipy.SpotifyException:
            print("No image available.")


