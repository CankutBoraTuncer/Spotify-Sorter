
class Artist:

    def __init__(self, artist_id):
        self._artist_id = artist_id
        self._artist_info = None
        self._genres = self._artist_info['genres'] 
    
    @classmethod
    def get_artist_id(self):
        return self._artist_id
    
    @classmethod
    def get_artist_info(self):
        return self._artist_info

    @classmethod
    def get_artist_genres(self):    
        return self._artist_genres
    
    @classmethod
    def get_artist_genre():
        return
    
    @classmethod
    def set_artist_id(self, artist_id):
        self._artist_id = artist_id  
        return
    
    @classmethod
    def set_artist_info(self, artist_info):
        self._artist_info = artist_info
        return