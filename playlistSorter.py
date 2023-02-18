from SpotifySorter import SpotifySorter

if __name__ == "__main__":

    # Variables
    client_id = '9d187d6237a542a9aaf72ab1bf705181'
    client_secret = 'ec7a2aa034824c77a6b20066b57c6c06'
    redirect_uri = 'http://localhost:8888/callback/'
    scope = "playlist-modify-public"
    username = "21u33vmd6canqa3zrspq6w6qq"
    target_playlist_uri = "spotify:playlist:6KeJfV2J3qWk1tXirvswuL"
    genre = "rock"
    playlist_name = "Pop Demo"
    playlist_description = ""
    
    
    # Initializing the spotify object
    spotify = SpotifySorter(client_id, client_secret, redirect_uri, scope)
    
    # Setting the username and the target playlist
    spotify.set_target_playlist(target_playlist_uri)
    spotify.set_username(username)
    
    spotify.initialize_spotify()
    
    # Retrieve tracks from the existing playlist
    spotify.load_playlist_tracks()
  
    spotify.create_playlist_by_genre(genre, playlist_name, playlist_description)
    
