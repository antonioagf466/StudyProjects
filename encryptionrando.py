#randomizing encryption and saving
#this code saves a json file for use on "encryptsusstain"
import string
import json
import random


def main():
    #filepath = "PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE"
    encryption = []
    for _ in range(10):
        encryption = encryption_key(encryption)
    save_encryption(filepath, encryption)
    
    
def save_encryption(filepath, encryption):
    data = {
        'encryption' : encryption
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
def encryption_key(encryption):
    key= " " + string.punctuation + string.digits + string.ascii_letters
    key = list(key)
    random.shuffle(key)
    number = len(encryption) + 1
    encryption.append({"key": key,"number": number })
    return encryption
           

if __name__ == "__main__":
    main()