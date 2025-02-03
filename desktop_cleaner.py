#this code sends your specified type of file from 1 folder(intended to be the desktop) to any other folder you desire
import os
import shutil


def clean_folder(folder_path):
    #foldergoal = 'PUT YOUR DESIRED FOLDER HERE AND UNCOMENT THIS LINE'
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension == "txt":
               file_path = os.path.join(folder_path, filename)
               shutil.move(file_path, foldergoal)
               print(f"The following file was moved to {foldergoal}: {file_path}")



def main():
    print("Desktop Cleaner Program")
    #folder_path = 'PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning complete")
    else:
        print("Invalid Folder path, please make sure the path given in a directory")



if __name__=="__main__":
    main()