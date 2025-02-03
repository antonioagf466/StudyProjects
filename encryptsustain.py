#if you want to use this code you need the "encryptionrando" to make the encryptions first and change the filepath on this code to where the json file is stored
import random
import string
import json


def main():
    chars= " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    #filepath = "PUT YOUR DESIRED FILEPATH HERE AND UNCOMENT THIS LINE"
    picked_number = input("Which encryption are we working with (1 - 10)?: ")
    if picked_number.isdigit() and int(picked_number) in range(1, 11): 
        picked_number = int(picked_number)
    else:
        picked_number = random.randrange(1,11)
        print(f"Your answer was not accepted but a number was randomized for you: {picked_number}")
        print(f"If you wish to decode a message instead of encrypting it, please make sure the numbers match")
    
    data = load_encryption(filepath)
    key = get_list_by_number(data, picked_number)
    #print (key)
    print("What would you like to do? ")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("*******************************")
    answer = input("Please select your answer (1/2): ")
    if answer == "1":
        print("Accepted characters: ")
        print(chars)
        text = input("Give a message do encrypt: ")
        encrypted_text = encrypt(chars, key, text)
        print(encrypted_text)
    elif answer == "2":
        print("Accepted characters: ")
        print(chars)
        text = input("Give a message do decrypt: ")
        decrypted_text = decrypt(chars, key, text)
        print(decrypted_text)
    else:
        print ("This was not a valid answer, the encryption program will turn off....")
        
def load_encryption(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found.......")   
    

            
def get_list_by_number(data, picked_number):
    encryption_list = data.get("encryption", [])
    for item in encryption_list:
        if item["number"] == picked_number:
            return item['key']
    

def encrypt(chars, key, text):
    encrypted_text = ""
    for letter in text:
        index = chars.index(letter)
        encrypted_text += key[index]
    return encrypted_text

def decrypt(chars, key, text):
    decrypted_text = ""
    for letter in text:
        index = key.index(letter)
        decrypted_text += chars[index]
    return decrypted_text
    
    
    
if __name__ == "__main__":
    print("Encryption test!")
    print ("****************")
    main()


