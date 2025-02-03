#youtube downloader
#DISCLAIMER: if youtube had any weird change that stopped this code from working I'm sorry :(
from pytubefix import YouTube

def main():
    #folder = "PUT YOUR DESIRED FOLDER HERE AND UNCOMENT THIS LINE"
    is_running = True
    while is_running:
        link = input("Give me the youtube link: ")
        print("Download in progress...")
        try:
            download(link, folder)
        except Exception:
            print("Something went wrong, please check if the link was right")
        go_again = input("Would you like to download another video?(Y/N): ").lower()
        if go_again == "y":
            pass
        else:
            is_running = False
    print("ENDING PROGRAM!")
    print("***************************")





def download(link, folder):
        video=YouTube(link)
        video=video.streams.get_highest_resolution()
        video.download(folder)
        print("Download completed!!")
        print("***************")
    

if __name__ == "__main__":
    main()