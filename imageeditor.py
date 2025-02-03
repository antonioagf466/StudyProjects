#image editor project
#this code applies the filter "sharpen" on all images on a specific folder and saves the images into another
from PIL import Image, ImageEnhance, ImageFilter
import os
def filter_images(path, pathout):
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")
        edit=img.filter(ImageFilter.SHARPEN)
        factor= 1.1
        enhancer=ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)
        
        clean_name=os.path.splitext(filename)[0]
        
        edit.save(f"{pathout}/{clean_name}_edited.jpg")




def main():
    #path ="PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE"
    #pathout= "PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE"
    filter_images(path,pathout)
        
    
    
if __name__ == "__main__":
    main()