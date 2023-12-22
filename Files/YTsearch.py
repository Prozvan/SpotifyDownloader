import yt_dlp

def getLink(SEARCH_QUERY):
   
    ydl_opts = {  #settings
        'quiet': True,
        'extract_flat': True,
        'max_results': 1,
    }
    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f'ytsearch{1}:{SEARCH_QUERY}', download=False)
    

    link = search_results["entries"][0]["url"]
    

    return link



