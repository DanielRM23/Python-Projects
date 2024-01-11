# Billboard-to-Spotify-Playlist

This Python script allows you to automatically create a private playlist on Spotify from the songs that were on the Billboard Hot 100 chart on a specific date. 
The user can input the date in the "YYYY-MM-DD" format to get the corresponding chart.


## Requirements

Before running the script, make sure to have the following dependencies installed:

- [Python](https://www.python.org/downloads/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/)

You can install Spotipy using the following command:

```bash
pip install spotipy


## Usage

1.- Run the billboard_to_spotify.py script.
2.- You will be prompted to enter the date in the "YYYY-MM-DD" format.
3.- The script will search for the songs that were on the Billboard Hot 100 chart for that date.
4.- An authentication window for Spotify will open. Log in and authorize the application.
5.- The script will create a new private playlist on your Spotify account with the name "YYYY-MM-DD Billboard 100".
6.- The found songs will be added to the newly created playlist.

Note: You will need to have a Spotify account and create an application on the Spotify Developer Dashboard to obtain the client ID and client secret, which are used in the authentication process.

## Configuration

Before running the script, make sure to edit the following code block in billboard_to_spotify.py with your own Spotify client ID and client secret:

python
Copy code
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_SPOTIFY_CLIENT_ID",
        client_secret="YOUR_SPOTIFY_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)


## Notes

The script uses Spotipy, a Python library for the Spotify API.
Make sure to comply with Spotify and Billboard's terms of service when using this script.


