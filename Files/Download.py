from pytube import YouTube


def downloadMusic(PATH, LINK, TRACK):

    
    yt = YouTube(LINK)
    audio = yt.streams.get_audio_only()
    try:
        audio.download(output_path=PATH, filename=TRACK+".mp3")

        print(f"\t\t\tDownloaded: {TRACK}.mp3")
    
    except FileExistsError: raise FileExistsError("File already exists!")




