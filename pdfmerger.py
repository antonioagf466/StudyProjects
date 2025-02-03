#pdf merger
#merges all pdfs from one folder and saves it on another

import PyPDF2
import sys
import os
import shutil

def mergepdfs(folder_path):
    #folder_goal = 'PUT YOUR DESIRED FOLDER HERE AND UNCOMENT THIS LINE'
    merger = PyPDF2.PdfMerger()
    for files in os.listdir(folder_path):
        if files.endswith(".pdf"):
            file_path = os.path.join(folder_path, files)
            merger.append(file_path)
    merged_pdf_path = os.path.join(folder_goal, 'Combinedpdfs.pdf')
    with open(merged_pdf_path, 'wb') as merged_file:
        merger.write(merged_file)
            



def main():
    #folder_path = 'PUT YOUR DESIRED FOLDER HERE AND UNCOMENT THIS LINE'
    if os.path.isdir(folder_path):
        mergepdfs(folder_path)
        print("merging complete")
    else:
        print("Invalid Folder path, please make sure the path given in a directory")


if __name__ == "__main__":
    main()
    