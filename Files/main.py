import SpotiyAPI
import YTsearch
import Download
from tkinter import filedialog
import tkinter as tk


def Type(link):
    if "album" in link: return "1"
    elif "playlist" in link: return "2"
    elif "artist" in link: return "3"
    else: return "0"

def CountControl(NUM):
    if NUM == "2": count = int(input("How many tracks? -> max(50): "))
    else: count = 1

    if count > 50:
        count = 50
        print("Too much, number of tracks is set defalt (50)!")

    return count


root = tk.Tk()  #creating a window => filedialog wouldn't work without it :/
root.withdraw()


print()
print("\t\t\t\t\tWelcome to Spotify Downloader!!")
print()
QUERY = input("\tLink (Album/Playlist/Artist (top songs)) => ")
print()


NUM = Type(QUERY)   # (Album, Playlist, Artist)

COUNT = CountControl(NUM)



if NUM in ["1", "2", "3"]:
    links = []
    status, tracks = SpotiyAPI.getMusic(QUERY, NUM, COUNT)

    if status== 0:
        
        print("\tProcess: GetMusic - Finished")
        print("\tProcess: GetLinkYT - Active")
        print()



        for track in tracks:
            
            track = track.replace("\"", "" )      # if there are ""
            
            link = YTsearch.getLink(track)           #Samo 200 klicev na dan
            links.append(link)
            print(f"\t\t\t{track}")
        

        print()
        print("\tProcess: GetLinkYT - Finished")
        print("\tProcess: Get Download Directory")
        print()

        
        DIR = filedialog.askdirectory(title="Select a directory")
        print("\t\t\tDownloading to: "+DIR)
        
        if DIR != "":
            print()
            print("\tProcess: Download - Active")
            print()
        
            for i in range(len(links)):

                Download.downloadMusic(DIR+"/", links[i], tracks[i])

            print()
            print("\tProcess: Download - Finished")
            print("\tEnjoy listening!")
            print()
        else:
            print()
            raise ValueError("Directory is not valid!")

    else:
        print()
        raise ConnectionError("Link doesn't lead to any Playlist/Album/Artist")
else:
    print()
    raise ValueError("Wrong Link!")

            

        




