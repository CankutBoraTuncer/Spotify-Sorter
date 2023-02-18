class Playlist:
    
    track_count = 0
   
    def __init__(self, playlist_id, playlist_name="", playlist_genre = ""):
        self._playlist_name = playlist_name
        self._playlist_id = playlist_id
        self._playlist_genre = playlist_genre
        self._playlist_tracks = []
        
    @classmethod
    def get_playlist_name(self):
        return self._playlist_name
    
    @classmethod
    def get_playlist_id(self):
        return self._playlist_id
    
    @classmethod
    def get_playlist_genre(self):
        return self._playlist_genre
    
    @classmethod
    def get_playlist_tracks(self):
        return self._playlist_tracks
    
    @classmethod  
    def track_exists(self, track_id):
        if (track_id in self._playlist_tracks.get_track_id()):
            return True
        return False
    
    @classmethod
    def update_playlist(self, track):
        self._playlist_tracks.append([track])
        print(self._playlist_tracks.length())
        return 
