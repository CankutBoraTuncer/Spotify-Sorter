import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Playlist import Playlist
from Track import Track
from pathlib import Path

class SpotifySorter:
    
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_uri = redirect_uri
        self._scope = scope
        self._spotify = None
        self._target_playlist_uri = None
        self._username = None
        self._target_playlist = None
        self._new_playlist = None
        
    def initialize_spotify(self):
        # Set up authentication using the Spotify API
        self._spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='9d187d6237a542a9aaf72ab1bf705181',
                                               client_secret='ec7a2aa034824c77a6b20066b57c6c06',
                                               redirect_uri='http://localhost:8888/callback/',
                                               scope='playlist-modify-public'))
            
    def set_target_playlist(self, target_playlist_uri, target_playlist_name):
        self._target_playlist_uri = target_playlist_uri
        self._target_playlist = Playlist(target_playlist_uri, target_playlist_name)
        return
       
    def set_username(self, username):
        self._username = username    
     
    def load_playlist_tracks(self):
        if(self.playlist_log_exists(self._target_playlist.get_playlist_name())):
            print("ads")
            self.load_tracks_from_txt(self._target_playlist.get_playlist_name())
        else:     
            results = self._spotify.user_playlist_tracks(self._username, self._target_playlist_uri)
            tracks = results['items']
            while results['next']:
                results = self._spotify.next(results)
                tracks.extend(results['items'])
            self.__update_target_playlist(self.__create_track_list(tracks))
        return 
    
    def create_playlist(self, playlist_name, playlist_description):
        playlist_id = self._spotify.user_playlist_create(user=self._username, name=playlist_name, public=True, description=playlist_description)['id']
        playlist = Playlist(playlist_id, playlist_name)
        self._new_playlist = playlist
        return 
    
    def set_artist_info(self, artist):
        artist_id = artist.get_artist_id
        artist_info = self._spotify.artist(artist_id)
        artist.set_artist_info(artist_info)
        return 
    
    def create_playlist_by_year(self, startingYear, endingYear, playlist_name, playlist_description = ""):
        self.create_playlist(playlist_name, playlist_description)
        tracks = self._target_playlist.get_playlist_tracks()
        for track in tracks:
            if(track.get_track_year() >= startingYear and track.get_track_year() <= endingYear):
                self._spotify.playlist_add_items(self._new_playlist.get_playlist_id(), [track.get_track_id()])
        return    
        
    def create_playlist_by_genre(self, genre, playlist_name, playlist_description = ""):
        self.create_playlist(playlist_name, playlist_description)
        tracks = self._target_playlist.get_playlist_tracks()
        for track in tracks:
            if(genre in track.get_track_genre()):
                self._spotify.playlist_add_items(self._new_playlist.get_playlist_id(), [track.get_track_id()])
        return    
    
    def save_tracks_to_txt(self):
        # Track(track_id, track_name, track_year, track_info)
        tracks = self._target_playlist.get_playlist_tracks()
        with open(f'{self._target_playlist.get_playlist_name()}.txt', 'w') as f:
            for track in tracks:
                try:
                    f.write(f'{track.get_track_id()},{track.get_track_name()},{track.get_track_year()},{track.get_track_info()}')
                    f.write('\n')
                except:
                    print(f'Error occured: - {track.get_track_name()}')
                    
    def load_tracks_from_txt(self, name):
        print(name)
        with open(f'{name}.txt', 'r') as f:
            while True:
                line = f.readline().strip().split(',')
                print(line)
                if not line:
                    self._target_playlist.update_playlist(Track(line[0],line[1],line[2],line[3]))
                    break
        
    def save_genres_to_txt(self):
        tracks = self._target_playlist.get_playlist_tracks()
        with open('genres.txt', 'w') as f:
            for track in tracks:
                try:
                    f.write(f'{track.get_track_name()} : {track.get_track_genre()}')
                    f.write('\n')
                except:
                    print(f'Error occured: - {track.get_track_name()}')
    
    def playlist_log_exists(self, name):
        path = Path(f'./{name}.txt')
        return path.is_file()
        
    def __update_target_playlist(self, tracks):
        for track in tracks:
            self._target_playlist.update_playlist(track)
        return
        
        
    def __create_track_list(self, tracks):
        track_objects = []
        for track in tracks:
            
            track_id = track['track']['id']
            track_name = track['track']['name']
            track_year = track['track']['album']['release_date']
            track_info = self._spotify.track(track_id)
            track = Track(track_id, track_name, track_year, track_info)
            if(track.set_track_genre(self._spotify.artist(track.get_artist_id())['genres'])):
                track_objects.append(track) 
        return track_objects