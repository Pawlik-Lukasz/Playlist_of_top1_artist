# Billboard Top Artist Spotify Playlist Creator

This project is designed to automate the process of creating a Spotify playlist featuring top hits from the Billboard chart-topping artist for a specified date. It utilizes web scraping techniques to gather data from the Billboard website and interacts with the Spotify API to create and customize playlists.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed on your system
- Dependencies installed via `pip install -r requirements.txt`
- Spotify Developer account and credentials (`CLIENT_ID`, `CLIENT_SECRET`, and `SPOTIFY_USERNAME`) stored in a `.env` file

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Pawlik-Lukasz/Playlist_of_top1_artist
```

2. Navigate to the project directory:
```bash
git cd Playlist_of_top1_artist
```
3. Set up your Spotify Developer credentials in a .env file:
```bash
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
SPOTIFY_USERNAME=your_spotify_username
```

## Usage
1. Run the script main.py:
``` bash
python main.py
```
2. Enter the date (in the format YYYY-MM-DD) from which you want to search for the top artist.

3. The script will then scrape the Billboard website to gather information about the top artist, including their name, top songs, and image.

4. Using the Spotify API, the script will create a playlist featuring the top songs of the artist obtained from Billboard.

5. Finally, the script will upload the artist's image as the playlist cover and delete the downloaded image.

## Customization
You can customize the project to suit your needs:

- Adjust the `AMOUNT_OF_SONGS` variable to change the number of top songs to include in the playlist.
- Modify the `create_playlist()` function to change the playlist name or add additional functionalities.

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.
