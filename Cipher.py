from ast import keyword
from ctypes.wintypes import MSG
import fileinput
from importlib.resources import path
import string
from xml.dom.expatbuilder import ElementInfo 
import importlib
import random
from pathlib import Path
import PySimpleGUI as ar




def cipher(text, move, alphabets):

    def shifted(alphabet):
        return alphabet[move:] + alphabet[:move]
    shifted = tuple(map(shifted, alphabets))
    donealph = ''.join(alphabets)
    doneshift = ''.join(shifted)
    table = str.maketrans(donealph, doneshift)
    return text.translate(table)



PickerMSG = (input("Press (1) for Text Encrypt/Decrypt | (2) for File Encrypt/Decrypt: "))
Answer = PickerMSG

# TEXT ENCRYPTION & DECRYPTION 

if Answer == "1":
    choice = input("Press (1) for Encryption | (2) for Decryption: ")
    if choice == "1":
        MSGINPut = input("ENTER MESSAGE: ")
        keycipher3 = int(input("Please Enter Key (0 - 25): "))
        FunctMSG = (cipher(MSGINPut, keycipher3, [string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits]))
        (print("ENCRYPTED MESSAGE: " + FunctMSG))
            
    if choice == "2":
        MSGINP = input("ENTER MESSAGE: ")
        keycipherinp = int(input("Please Enter Your Chosen Key: "))
        DECMSG = (cipher(MSGINP, -keycipherinp, [string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits]))
        print("DECRYPTED MESSAGE: " + DECMSG)
            


# FILE ENCRYPTION & DECRYPTION 

if Answer == "2":

    file_enc_dec = input("Press (1) for File Encryption | (2) for Decryption: ")
    
    if file_enc_dec == "1":
        generated_key =''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))

        fileopen = ar.popup_get_file("Select Your File", file_types=(("Text Files", "*.txt*"),),)
        if not fileopen:
            ar.popup("No File Selected")
        else:
            ar.popup("You have Successfully selected your file !")

        userinput = open('Secretkey.txt', 'w+')
        userinput.write(generated_key)

        #file encryption

        file_to_encrypt = Path(fileopen).read_text()
    

        FunctMSG2 = (cipher(file_to_encrypt, 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))
    
        encrypted_info = open('ENCRYPTEDFILE.txt', 'w')
        encrypted_info.write(FunctMSG2)
        print("Generated Key: " + generated_key)

        print("------Your file has been ecrypted & your randomly generated key is saved------")
    
    if file_enc_dec == "2":
        generated_key =''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))

        fileopendec = ar.popup_get_file("Select Your File", file_types=(("Text Files", "*.txt*"),),)
        if not fileopendec:
            ar.popup("No File Selected")
        else:
            ar.popup("You have Successfully selected your file !")

        file_to_decrypt = Path(fileopendec).read_text()
        
        key_input = input("Please Enter The Key: ")
        read_key_file = Path('Secretkey.txt').read_text()
        if key_input == read_key_file:
            FunctMSG3 = (cipher(file_to_decrypt, -3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation, string.digits]))   
            decrypted_info = open('DECRYPTEDFILE.txt', 'w')
            decrypted_info.write(FunctMSG3)
            print("------Your File Has Been Decrypted !!------")
        else:
            print("------You Have Entered the WRONG Key------") 