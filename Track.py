class Track:
    
    def __init__(self, track_id, track_name, track_year, track_info):
        self._track_id = track_id
        self._track_name = track_name
        self._track_year = track_year
        self._track_info = track_info
        self._track_artist = None
        self._artist_id = 0
        self._track_genre = None
        if len(self._track_info['artists']) > 0:    
            self._track_artist = self._track_info['artists'][0]['name']
            self._artist_id = self._track_info['artists'][0]['id']
        
    def get_track_id(self):
        return self._track_id
    
    def get_track_name(self):
        return self._track_name  
        
    def get_track_year(self):
        return int(self._track_year[0:4])
    
    def get_track_info(self):
        return self._track_info
    
    def get_track_artists(self):
        return self._track_id
    
    def get_track_info(self):
        return self._track_id
    
    def get_artist(self):
        return self._artist
    
    def get_track_genre(self):
        return self._track_genre
    
    def get_artist_id(self):
        return self._artist_id
    
    def set_track_genre(self, genre):
        try: 
            self._track_genre = genre[0]  
            return True;
        except IndexError as ie:
            print(f"Error occured: {ie} - {self._track_name}")
            print(genre)
            return False;
            
        
        
    
