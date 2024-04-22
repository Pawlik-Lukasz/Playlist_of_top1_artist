from Scraper import BillboardScraper
from Spotify import SpotifyManager
from dotenv import load_dotenv
from GUI import PlaylistCreatorGUI
import os
from pathlib import Path
import time


load_dotenv(".env")
CLIENT_ID = os.getenv("CLIENT_ID")  # client id for spotipy API
CLIENT_SECRET = os.getenv("CLIENT_SECRET")  # client secret for spotipy API
USERNAME = os.getenv("SPOTIFY_USERNAME")  # username for Spotify account
AMOUNT_OF_SONGS = 20

def scrape_data(input_date):
    # scraping info about top artist from billboard page for given date
    scraper = BillboardScraper(date=input_date)
    # get artist name from Billboard page
    artist_name = scraper.top_artist_name_title()
    # get endpoint for given artist name
    artist_name_endpoint = scraper.top_artist_name_endpoint()
    # get image from artist Billboard page
    artist_img = scraper.scrape_img_url()["img"]
    artist_songs = scraper.scrape_top_songs(amount_of_songs=AMOUNT_OF_SONGS)

    # make dictionary containing all important variables
    scraped = {
        "artist_name": artist_name,
        "artist_name_endpoint": artist_name_endpoint,
        "artist_img": artist_img,
        "artist_songs": artist_songs,
        "path_to_img":  Path(scraper.scrape_img_url()["path"])

    }
    return artist_name, artist_name_endpoint, artist_img, artist_songs, Path(scraper.scrape_img_url()["path"])


def create_playlist(name, songs, image):
    # creating playlist that contains given amount of top hits songs from top artist for given date
    sp_manager = SpotifyManager(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, username=USERNAME)
    sp_manager.authorize_spotify()
    sp_manager.get_songs_uris(top_artist_name=name, top_songs=songs)
    sp_manager.create_playlist(top_artist_name=name, amount_of_songs=AMOUNT_OF_SONGS)
    sp_manager.add_tracks_to_playlist()
    sp_manager.upload_cover_image(img_base64=image)


if __name__ == "__main__":

    app = PlaylistCreatorGUI()
    app.mainloop()
    username, input_date = app.playlist_created()
    artist_name, artist_name_endpoint, artist_img, artist_songs, path_to_img = scrape_data(input_date=input_date)
    create_playlist(name=artist_name, songs=artist_songs,
                    image=artist_img)
    # wait 3 seconds (for playlist being created) and delete image from images folder
    time.sleep(3)
    path_to_img.unlink()
