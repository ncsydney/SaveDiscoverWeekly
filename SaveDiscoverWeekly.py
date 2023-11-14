from refresh import Refresh
import requests
import secret

class SaveSong:
    def __init__(self):
        self.spotify_token = ""
        self.tracks = []

    def call_refresh(self):
        refreshCaller = Refresh()
        self.spotify_token = refreshCaller.refresh()

    def fetch_songs_in_playlist(self):
        get_all_songs = requests.get(
            f"https://api.spotify.com/v1/playlists/{secret.discover_weekly_id}/tracks", 
            headers={"Authorization": f"Bearer {self.spotify_token}"})
        
        json_songs = get_all_songs.json()
        for song in json_songs['items']:
            self.tracks.append(f"{song['track']['uri']}")
        return self.tracks
      
    def add_songs_to_playlist(self):
        songs = {'uris': self.tracks}
        save_discover_weekly_playlist = f"https://api.spotify.com/v1/playlists/{secret.save_discover_weekly_id}/tracks"
        add = requests.post(save_discover_weekly_playlist, 
                            json=songs, headers={'Authorization': f'Bearer {self.spotify_token}'})
        return add.json()

a = SaveSong()
a.call_refresh()
a.fetch_songs_in_playlist()
a.add_songs_to_playlist()