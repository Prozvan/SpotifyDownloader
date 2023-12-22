import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def GetTitle(artists, SongName):

    if "Remix" in SongName: SongName = SongName.replace("- ", "(") +")"

    full_name = artists +" - " + SongName    #Celo ime
    songs.append(full_name)



def getMusic(LINK, NUM, COUNT):
    CLIENT_ID = "9717e2e3a189466990a23fc7a0128bc8"
    CLIENT_SECRET = "44817ba8434840ec8db6243a0849f809"
   
    

    #Registration
    client_credits_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    #Session
    session = spotipy.Spotify(client_credentials_manager=client_credits_manager)



    Links = [r"https://open.spotify.com/album/(.*)\?",
             r"https://open.spotify.com/playlist/(.*)\?",
             r"https://open.spotify.com/artist/(.*)\?"]
    
    
   
    if match := re.match(Links[int(NUM)-1], LINK):
        playlist_uri = match.groups()[0]            #without prefix

    else: 
        print()
        print(f"\tError => Expected format: {Links[int(NUM)-1][:len(Links[int(NUM)-1])-6]}...")
        print()
        quit()



    #Checks if there are any errors
    try:
        if NUM == "1": tracks = session.album_tracks(playlist_uri)["items"]  #album
        elif NUM == "2": tracks = session.playlist_tracks(playlist_uri, limit=COUNT)["items"] #playlist
        elif NUM == "3": tracks = session.artist_top_tracks(playlist_uri)["tracks"] #artist
        
    except spotipy.SpotifyException: return 1, []


    global songs
    songs = []

    if NUM == "1":            #Album
        for track in tracks:
            SongName = track["name"]  

                
            artists = ", ".join([
                artist["name"] for artist in track["artists"]
            ])

            GetTitle(artists, SongName)

    elif NUM == "2":  #Playlist

        for track in tracks:
            SongName = track["track"]["name"]  
                
            artists = ", ".join([
                artist["name"] for artist in track["track"]["artists"]
            ])

            GetTitle(artists, SongName)
            
    elif NUM == "3":                 #artist
        for track in tracks:    
            SongName = track["name"]

            artists = ", ".join([ 
                artist["name"] for artist in track["artists"]
                ])
            
            GetTitle(artists, SongName)
            

    return 0, songs







