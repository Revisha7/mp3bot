from pytube import YouTube, Playlist
import os
def check_title(title):
    index = title.find('\\')
    index2 = title.find('/')
    while index != -1 or index2 != -1:  
        return False
    return True

def get_title():
    title = str(input("Input the name for the mp3 file (Original video title will be used if given no input): "))
    while check_title(title) is False:
        title = input("Your file name can't contain '\' or '/' Please enter a new title: ")
    return title

def download_vid(yt,option=2, saveAddress='', original = 2):
    print(f"Video: {yt.title}")

    if original == 1:
        title = check_title(yt.title)
    else:
        title = get_title()
        if (title == ""):
            title = yt.title
        
    print("Loading video...")
    streamlist = yt.streams.filter(only_audio=True).order_by("abr")
    print("Video loaded!")
    
    

    if option == 2:
        for stream in range(len(streamlist)):
            print("Options: ")
            print(f"Option {stream+1} - Bitrate: {streamlist[stream].abr} File Size: {streamlist[stream].filesize_mb} mb")
        option = int(input("Enter the option number to download: "))
        mp3file = yt.streams.get_by_itag(streamlist[option-1].itag)
    else:
        mp3file = yt.streams.get_by_itag(streamlist[-1].itag)
    
    if saveAddress == '':
        saveAddress = input("Enter the filepath to save the file (Will be saved in same folder as code if given no input): ")

    done = False
    while done is False:
        try:
            if saveAddress != "":
                mp3file.download(filename = f"{title}.mp3", output_path = saveAddress)
                
            else:
                mp3file.download(filename = f"{title}.mp3")
            done = True
        except:
            title = input("Your file name isn't valid! Please enter a new title that abides your os guidelines of file naming (Try removing special characters)")
    print(f"Saved {title}!")

    return

def getlink_vid(correct = 0):
    while correct != 1:
        link = input("Please enter the link to the video you wish to download as an audio file: ")
        yt = YouTube(link)
        correct = checkCorrectLink_vid(yt)
    return yt

def checkCorrectLink_vid(yt):
    #add try and catch for if user inputs something that cant be turned into int
    number = int(input(f"Is this the correct video? Enter 1 for 'yes' and 2 for 'no' [{yt.title}]"))
    while number != 1:
        if number == 2:
            return 2
        else:
            number = int(input(f"Invalid input. Please enter 1 if this is the correct video, and 2 if not [{yt.title}]"))
    return 1

def checkCorrectLink_pl(pl):
    #add try and catch for if user inputs something that cant be turned into int
    number = int(input(f"Is this the correct playlist? Enter 1 for 'yes' and 2 for 'no' [{pl.title}: {pl.length} videos]"))
    while number != 1:
        if number == 2:
            return 2
        else:
            number = int(input(f"Invalid input. Please enter 1 if this is the correct playlist, and 2 if not [{pl.title}]"))
    return 1


def getlink_pl(correct = 0):
    while correct != 1:
        link = input("Please enter the link to the playlist you wish to download as audio files: ")
        pl = Playlist(link)
        correct = checkCorrectLink_pl(pl)
    return pl

def download_pl(pl):
    original = input("Enter 1 to use the original video title for the file name for all videos, and 2 to use your own titles (You might have to use your own title for certain videos that have special characters suhc as front or backwards slashes): ")
    bitrateOption = input("Enter 1 to download using the highest audio quality for all videos in the playlist, and 2 if you want to make individual selections: ")
    saveAddress = input("Enter the filepath to save all files (Give no input if you would like to choose separately for individual videos): ")
    for vid in pl.videos:
        download_vid(vid, bitrateOption, saveAddress, original = original)
    print(f"Downloading all videos from {pl.title} complete!")



def vid_or_pl():
    choice = int(input("Enter 1 to download 1 video, or 2 to download videos in a playlist: "))
    if choice == 1:
        yt = getlink_vid()
        download_vid(yt, option = 2)
    elif choice == 2:
        pl = getlink_pl()
        download_pl(pl)





def run():
    print("Hello! Welcome to the Youtube Mp3 Bot.")
    vid_or_pl()


if __name__ == "__main__":
    run()