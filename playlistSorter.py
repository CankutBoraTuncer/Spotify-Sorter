from SpotifySorter import SpotifySorter

if __name__ == "__main__":

    # Variables
    client_id = '9d187d6237a542a9aaf72ab1bf705181'
    client_secret = 'ec7a2aa034824c77a6b20066b57c6c06'
    redirect_uri = 'http://localhost:8888/callback/'
    scope = "playlist-modify-public"
    username = "21u33vmd6canqa3zrspq6w6qq"
    # My uri's
    # spotify:playlist:09RwtIwcSjkWEHyupYGdVw - Bon Apetite
    # spotify:playlist:42ZyLJ4MOraf6XyQcuGaTd - Busy
    # spotify:playlist:1bOgdN2bFIZY9ntebzeYz5 - Just Sad Bro
    # spotify:playlist:4vaqbpkTiEIySH5w8nxCl1 - Parallel Park
    target_playlist_uri = "spotify:playlist:09RwtIwcSjkWEHyupYGdVw"
    genre = "turkish"
    startingYear = 1970
    endingYear = 1995
    playlist_name = "Old but gold"
    playlist_description = "Playlist created using Spotify API and Python - Cankut Bora Tuncer"
    
    
    # Initializing the spotify object
    sps = SpotifySorter(client_id, client_secret, redirect_uri, scope)
    
    # Setting the username and the target playlist
    sps.set_target_playlist(target_playlist_uri)
    sps.set_username(username)
    
    sps.initialize_spotify()
    
    # Retrieve tracks from the existing playlist
    sps.load_playlist_tracks()
    
    # Save genres to a txt file
    sps.save_genres_to_txt()
    
    # Create a new playlist from an existing playlist according to the selected genre
    sps.create_playlist_by_genre(genre, playlist_name, playlist_description)
    
    # Retrieve tracks from the existing playlist
    sps.create_playlist_by_year(startingYear, endingYear, playlist_name, playlist_description)
