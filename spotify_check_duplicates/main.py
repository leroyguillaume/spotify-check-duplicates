from spotipy import Spotify, SpotifyOAuth

LIMIT = 50


def main():
    auth = SpotifyOAuth(scope="user-library-read")
    spotify = Spotify(auth_manager=auth)
    titles = {}
    offset = 0
    page = spotify.current_user_saved_tracks(LIMIT, offset)
    count = 0
    while page["next"]:
        for item in page["items"]:
            title = item["track"]["name"].lower()
            if title in titles:
                titles[title] += 1
            else:
                titles[title] = 1
        offset += LIMIT
        count += 1
        page = spotify.current_user_saved_tracks(LIMIT, offset)
    for title, count in titles.items():
        if count > 1:
            print(f"{title}: {count}")
