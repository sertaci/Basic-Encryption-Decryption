#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Basic, dummy encryption based on Caesar cipher method.
It uses basic keys such as 314, 271, 161, 662.
These are the first 3 digits of some constants in the universe.
Pi, euler, golden ratio, and planck constant
"""

"""
----------------------------------------------------------------------------
Created By  : Sertac İnce
Created Date: 26/08/2022
Updated Date: 28/05/2023
version ='i.314.271.161.662'
---------------------------------------------------------------------------
"""


import string
import re
import subprocess


def menuPrinter():
    """Helper function for printing menu.
    """

    print("\n\n" + "*" * 27)
    print("\tCRYPT MENU")
    print("*" * 27)
    print("\n1. ENCRYPT \n2. DECRYPT \n3. EXIT\n")
    print("*" * 27, end="\n\n")


def modePrinter(mode : str):
    """Helper function for printing mode menu.
    """

    print("\n" + "*" * 27)
    print(f"\t {mode.upper()}")
    print("*" * 27, end="\n\n")


def menuOptionCast() -> int:
    """Check whether the chosen main menu option can be casteble to integer.
    """

    try:
        option = int(input("Choose an option: "))
        return option
    except:
        print("Wrong option!")
        return -1
   
            
def menuChecker(option : int) -> int:
    """Check if the option is in the list.
    """

    if option not in [1, 2, 3]:
        print("Wrong option!")
        return -1
    
    elif option == 3:
        exit()

    # Returning the crypt or decrypt mode (1 or 2)
    else:    
        return option


def mainMenu() -> int:
    """Main menu controller
    """

    menuPrinter()
    while(True):
        option = menuOptionCast()

        if option == -1:
            continue

        validOption = menuChecker(option)
        if validOption == -1:
            continue

        return validOption        


def encryptFoo(text : str, key : int, lowerCase : list) -> str:
    """ Crypting function. Basically it uses caesar cipher method.
    If it exceeds the lowercase alphabet, basically it makes some modulo operation.
    """

    crypted = ""

    for i in text:
        a = ord(i) + (key % 26)
        if a > 122:
            crypted += lowerCase[a % 122]

        else:
            crypted += chr(a)

    return crypted


def decryptFoo(text : str, key : int, lowerCase : list) -> str:
    """ Derypting function. Reverse of the encrypt function
    """

    decrypted = ""

    for i in text:
        a = ord(i) - (key % 26)

        if a < 97:
            decrypted += lowerCase[122 - (97 % a) - 97]

        else:
            decrypted += chr(a)

    return decrypted


def noChoiceAction() -> int:
    """When user do not like the result of trimmed string, this function is called
    """

    try:
        print("*" * 23)
        print("\n1. Re-enter text\n2. Back to menu")
        print("\n" + "*" * 23)
        noCase = int(input("\nChoose an option: "))
        print("")
        
        if noCase == 1 or noCase == 2:
            return noCase
        
        else:
            print("Wrong option!")
            return -1
        
    except:
        print("Wrong option!")
        return -2
    

def cleanText(text : str) -> str:
    """Convert input text to lowercase characters.
    """

    text = re.sub("[^a-zA-Z]", "", text)
    text = text.lower().strip()

    return text


def getText() -> str:
    """Getting the input text and clean it for the encryption or decryption.
    """

    while (True):
        text = input("Enter the text as adjacent lowercase characters (or it will be lowercased and truncated): ")
        text = cleanText(text)

        textConfirmation = input(f"\nText will be: {text}\nIs it okay? (y/n): ")
        print("")
        if textConfirmation == "y" or textConfirmation == '\n':
            return text
        
        noChoice = noChoiceAction()
        if noChoice == -1 or noChoice == -2:
            noChoice = noChoiceAction()

        elif noChoice == 1:
            continue
        else:
            main()


def getKey() -> int:
    """ Getting the proper key until the proper key is entered.
    """

    key = int(input("Enter the key: "))
    keyList = [314, 271, 161, 662]

    while key not in keyList:
        print("Wrong key!")
        key = int(input("Re-enter the key: "))

    print("")
    return key    


def copyClipBoard(text):
    """Copy result to the clipboard.
    """

    command = 'echo '+ text + '|clip'
    return subprocess.check_call(command, shell=True)


def main():
    """Main function for processing all the functions
    """
    cryptOption = mainMenu()
    lowerCase = list(string.ascii_lowercase)

    if cryptOption == 1:
        modePrinter("encryption")

        text = getText()
        key = getKey()

        crypted = encryptFoo(text, key, lowerCase)

        print(f"Crypted text: {crypted}")
        input("Press enter to copy crypted text to the clipboard and go to the menu.")

        copyClipBoard(crypted)
        main()

    else:
        modePrinter("decryption")

        text = getText()
        key = getKey()

        decrypted = decryptFoo(text, key, lowerCase)

        print(f"Derypted text: {decrypted}")
        input("Press enter to copy decrypted text to the clipboard and go to the menu.")
        
        copyClipBoard(decrypted)
        main()


if __name__ == '__main__':
    main()

