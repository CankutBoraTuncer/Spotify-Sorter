from SpotifySorter import SpotifySorter

if __name__ == "__main__":

    # Variables

    # My uri's
    # spotify:playlist:09RwtIwcSjkWEHyupYGdVw - Bon Apetite
    # spotify:playlist:42ZyLJ4MOraf6XyQcuGaTd - Busy
    # spotify:playlist:1bOgdN2bFIZY9ntebzeYz5 - Just Sad Bro
    # spotify:playlist:4vaqbpkTiEIySH5w8nxCl1 - Parallel Park
    target_playlist_uri = "spotify:playlist:09RwtIwcSjkWEHyupYGdVw"
    target_playlist_name = "Bon Apetite"
    genre = "turkish"
    startingYear = 1995
    endingYear = 2010
    playlist_name = "2000s"
    playlist_description = "Playlist created using Spotify API and Python - Cankut Bora Tuncer"
    
    
    # Initializing the spotify object
    sps = SpotifySorter(client_id, client_secret, redirect_uri, scope)
    
    # Setting the username and the target playlist
    sps.set_target_playlist(target_playlist_uri, target_playlist_name)
    sps.set_username(username)
    
    sps.initialize_spotify()
    
    # Retrieve tracks from the existing playlist
    sps.load_playlist_tracks()
    
    # sps.save_tracks_to_txt()
    
    # Save genres to a txt file
    # sps.save_genres_to_txt()
    
    # Create a new playlist from an existing playlist according to the selected genre
    # sps.create_playlist_by_genre(genre, playlist_name, playlist_description)
    
    # Create a new playlist from an existing playlist according to the selected starting and ending year
    sps.create_playlist_by_year(startingYear, endingYear, playlist_name, playlist_description)
