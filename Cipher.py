
# Import string used to import character library which is used within the code as alphabets (uppercase, lowercase & special characters & digits)
# Import random used to generate the random key, .randit is used to generate a digit within the range of (0-25)
# Pathlib is used to read file paths
# PysimpleGUI is used to create a GUI to request user file 

import string
import random
from pathlib import Path
import PySimpleGUI as ar



# Definition "cipher", used to encode and decode both text and files

def cipher(text, move, alphabets):
    #shifted def is to shift alphabet   
    # return alphabet starting from and ending at the key (shift)
    def shifted(alphabet):
        # creating a new alphabet starting at the character of the key number 
        # until the end of the alphabets as well as the characters before the character of the key numbers

        return alphabet[int(move):] + alphabet[:int(move)]
    #mapping the shifted alphabet with the character list then joining them
    shifted = tuple(map(shifted, alphabets))
    donealph = ''.join(alphabets)
    doneshift = ''.join(shifted)
    #creating a mapping table that is used with (.translate) to replace characters  
    table = str.maketrans(donealph, doneshift)
    return text.translate(table)


print("------------------------------------ CAESAR'S CIPHER PROGRAM ------------------------------------")


PickerMSG = (input("Press (1) for Text Encrypt/Decrypt | (2) for File Encrypt/Decrypt: "))
Answer = PickerMSG

# TEXT ENCRYPTION & DECRYPTION 
# if function used to seperate different actions within the encryption program
if Answer == "1":
    choice = input("Press (1) for Encryption | (2) for Decryption: ")
    if choice == "1":
        usrencryptmessage = input("ENTER MESSAGE: ")
        # random.choices is applied to generate a random integer of "1-26" characters which is the key
        randomkey = random.randint(1,26)
        print("YOUR CHOSEN KEY IS: " + str(randomkey))
        # the cipher definition was called to encrypted the inputted text, which is then printed as the encrypted message
        encodedmessage = (cipher(usrencryptmessage, randomkey, [string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits]))
        (print("ENCRYPTED MESSAGE: " + encodedmessage))
            #if the user chose to decrypt text the same defintion 
            # would be called but in this case the key has to be 
            # negative to shift back the character to its original place
    if choice == "2":
        decmessage = input("ENTER MESSAGE: ")
        keyintake = int(input("PLEASE ENTER YOUR CHOSEN KEY: "))
        decodedmessage = (cipher(decmessage, -keyintake, [string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits]))
        print("DECRYPTED MESSAGE: " + decodedmessage)
            


# FILE ENCRYPTION & DECRYPTION 

if Answer == "2":

    file_enc_dec = input("Press (1) for File Encryption | (2) for Decryption: ")
    
    if file_enc_dec == "1":
        # random key is generated using random.choices which 
        # is imported from random, using the lower & upper case alphabets with a 16 character range

        generated_key =''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))

        #popup_get_file is used to create a GUI to request file, 
        # PysimpleGUI is used and imported as ar which was used below to 
        # call popup_get_file to open a GUI requesting the file the user would like to decrypt

        fileopen = ar.popup_get_file("Select Your File", file_types=(("Text Files", "*.txt*"),),)
        
        #if statment used here incase file not selected or operation is cancelled else another GUI promt would appear with the message below

        if not fileopen:
            ar.popup("No File Selected")
        else:
            ar.popup("You have Successfully selected your file !")

        #opening a file as "secretkey.txt" and writing the generated key 

        userinput = open('Secretkey.txt', 'w+')
        userinput.write(generated_key)

        # opening & reading the fileopen which is the user selected file

        file_to_encrypt = Path(fileopen).read_text()
    
        # using the cipher definition to encrypt the file text content with a shift of 3 

        Encrypting = (cipher(file_to_encrypt, 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))

        # opening a new file as "Encryptedfile.txt" and writing the encrypted text 

        encrypted_info = open('Encryptedfile.txt', 'w')
        encrypted_info.write(Encrypting)

        # printing the generated key as well as a message to assure the user that their file has been decrypted 

        print("Generated Key: " + generated_key)

        print("------Your file has been ecrypted & your randomly generated key is saved------")

    
    if file_enc_dec == "2":

        # generating a random key within a 16 digit range as done in the file encryption process

        generated_key =''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))

        # GUI is then used to request file as done in the encryption process

        fileopendec = ar.popup_get_file("Select Your File", file_types=(("Text Files", "*.txt*"),),)
        if not fileopendec:
            ar.popup("No File Selected")
        else:
            ar.popup("You have Successfully selected your file !")

        # opening & reading the fileopen which is the user selected file

        file_to_decrypt = Path(fileopendec).read_text()
        
        # the key is then requested from the user to decrypt the file content to its original form, 
        # if the wrong key is inputted the user would be notified that they have entered the wrong key

        key_input = input("Please Enter The Key: ")

        # Opening & reading the Key that is saved as a text file from the encryption process

        read_key_file = Path('Secretkey.txt').read_text()

        # if statment made to make sure the correct key was written else the user would be notified that they have entered the wrong key

        if key_input == read_key_file:

            # cipher definition is called to decrypt the file with a shift of -3 

            decrypting = (cipher(file_to_decrypt, -3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))   
            
            # opening a new file as "Decryptedfile.txt.txt" and writing the decrypted text, then notified the user that their file has been decrypted
            
            decrypted_info = open('Decryptedfile.txt', 'w')
            decrypted_info.write(decrypting)
            print("------Your File Has Been Decrypted------")
        else:
            print("------You Have Entered the WRONG Key------") 

    # Code written by Omar Ali CU2100723.
