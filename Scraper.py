from bs4 import BeautifulSoup
import requests
import base64


class BillboardScraper:
    BILLBOARD_ENDPOINT = "https://www.billboard.com/"
    BILLBOARD_SONGS_END = "/chart-history/hsi/"

    def __init__(self, date):
        self.top_artist = ""
        self.top_artist_formatted = ""
        self.top_songs = ""
        self.img_url = ""
        self.img64 = ""
        self.top_songs_formatted = []
        # main billboard endpoint for given date
        billboard_artists_endpoint = BillboardScraper.BILLBOARD_ENDPOINT + "/charts/artist-100/" + date + "/"
        artists_page = requests.get(billboard_artists_endpoint, "html.parser")
        self.artists_soup = BeautifulSoup(artists_page.content, "html.parser")

    def top_artist_name_title(self):
        # scraping top artist name for given date
        self.top_artist = self.artists_soup.select_one("div.o-chart-results-list-row-container"
                                                       " li.lrv-u-width-100p ul li h3")
        self.top_artist = self.top_artist.getText().strip()
        return self.top_artist

    def top_artist_name_endpoint(self):
        self.top_artist = self.artists_soup.select_one("div.o-chart-results-list-row-container"
                                                       " li.lrv-u-width-100p ul li h3")
        self.top_artist = self.top_artist.getText().strip()
        # formatting artist name to later use it for endpoint
        self.top_artist_formatted = self.top_artist.lower().replace(" ", "-")
        return self.top_artist_formatted

    def scrape_img_url(self):
        # scrape img from Billboard
        self.img_url = self.artists_soup.select_one("div.c-lazy-image div img").attrs["data-lazy-src"]
        img_response = requests.get(self.img_url)
        # taking last element of url, so we will name our file with artist's name
        name_of_file = self.img_url.split('/')[-1]
        # creating a file and converting img to base64
        with open(name_of_file, "wb") as file:
            file.write(img_response.content)
        with open(name_of_file, "rb") as file:
            data = file.read()
            self.img64 = base64.b64encode(data)

        # make dictionary with path to the image and the image:
        name_and_img = {
            "path": name_of_file,
            "img": self.img64
        }
        return name_and_img

    def scrape_top_songs(self, amount_of_songs):
        # billboard page endpoint for top artist
        billboard_songs_endpoint = (BillboardScraper.BILLBOARD_ENDPOINT + "artist/"
                                    + self.top_artist_formatted + BillboardScraper.BILLBOARD_SONGS_END)
        songs_page = requests.get(billboard_songs_endpoint, "html.parser")
        songs_soup = BeautifulSoup(songs_page.content, "html.parser")
        # scrape top songs for top artist
        self.top_songs = songs_soup.find_all("h3", class_="a-no-trucate", limit=amount_of_songs)
        return [song.getText().strip() for song in self.top_songs]



