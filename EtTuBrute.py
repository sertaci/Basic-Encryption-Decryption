#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Basic, dummy encryption based on Caesar cipher method.
It uses basic keys such as 314, 271, 161, 662.
These are the first 3 digits of some constants in the universe.
Pi, euler, golden ratio, and planck constant.
Et Tu, Brute?
"""

"""
----------------------------------------------------------------------------
Created By  : Sertac İnce
Created Date: 26/08/2022
Updated Date: 28/05/2023
Version: 'i.314.271.161.662'
---------------------------------------------------------------------------
"""


import string
import re
import subprocess
import platform
import time


class EtTuBrute():
    _keyList = []
    _lowerCase = []
    def __init__(self):
        self._keyList = [314, 271, 161, 662]
        self._lowerCase = list(string.ascii_lowercase)


    def encryptFoo(self, text: str, key: int, lowerCase: list, spaceOpt: bool = False) -> str:
        """Crypting function. Basically it uses caesar cipher method.
        If it exceeds the lowercase alphabet, basically it makes some modulo operation.
        """

        crypted = ""

        for letter in text:
            # For the whitespaces 
            if not spaceOpt and letter == " ":
                crypted += " "
                continue

            a = ord(letter) + (key % 26)
            if a > 122:
                crypted += lowerCase[a % 122-1]

            else:
                crypted += chr(a)

        return crypted


    def decryptFoo(self, text: str, key: int, lowerCase: list, spaceOpt: bool = False) -> str:
        """Derypting function. Basically reverse of the encrypt function"""

        decrypted = ""

        for letter in text:
            # For the whitespaces 
            if not spaceOpt and letter == " ":
                decrypted += " "
                continue

            a = ord(letter) - (key % 26)

            if a < 97:
                decrypted += lowerCase[26 - (97 % a)]

            else:
                decrypted += chr(a)

        return decrypted


    def noChoiceAction(self) -> int:
        """When user do not like the result of trimmed string, this function is called"""

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


    def cleanText(self, text: str, spaceOpt: bool = False) -> str:
        """Convert input text to lowercase characters."""

        pattern = "[^a-zA-Z ]"
        if spaceOpt:
            pattern = "[^a-zA-Z]"

        text = re.sub(pattern, "", text)
        text = text.lower() 

        return text


    def getSpaceOption(self) -> bool:
        spaceOptConf = input("\nDo you want whitespace characters to be deleted? (y/n): ")
        print("")

        if spaceOptConf == "y" or spaceOptConf == "\n":
            return True
        
        print("Whitespace characters will not be deleted because 'no' option is selected (or wrong option is selected)")
        return False



    def getText(self) -> tuple:
        """Getting the input text and clean it for the encryption or decryption."""

        while True:
            text = input(
                "Enter the text as lowercase characters (or it will be lowercased): "
            )
            spaceOpt = self.getSpaceOption()
            text = self.cleanText(text, spaceOpt)

            textConfirmation = input(f"\nText will be: {text}\nIs it okay? (y/n): ")
            print("")
            if textConfirmation == "y" or textConfirmation == "\n":
                return (text, spaceOpt)

            noChoice = self.noChoiceAction()
            if noChoice == -1 or noChoice == -2:
                noChoice = self.noChoiceAction()

            elif noChoice == 1:
                continue
            else:
                self.run()


    def getKey(self) -> int:
        """Getting the proper key until the proper key is entered."""
        try:
            key = int(input("Enter the key: "))
        except:
            self.getKey()

        while key not in self._keyList:
            print("Wrong key!")
            self.getKey()

        print("")
        return key


    def copyClipBoard(self, text) -> None:
        """Copy result to the clipboard."""

        command = "echo " + text + "|clip"
        return subprocess.check_call(command, shell=True)
    

    def checkOS(self, message: str):
        # If the system is Windows, call the unique win command executer function to copy clipboard 
        if platform.system() == "Windows":
            input(
                "Press enter to copy text to the clipboard and go to the menu."
            )
            self.copyClipBoard(message)
        else:
            input("Press enter to go to the menu ")


    def menuChecker(self, option: int) -> int:
        """Check if the option is in the list."""

        if option not in [1, 2, 3]:
            print("Wrong option!")
            return -1

        elif option == 3:
            print("\nExitting...")
            time.sleep(2)

            exit()

        # Returning the crypt or decrypt mode (1 or 2)
        else:
            return option


    def menuOptionCastable(self) -> int:    
        """Check whether the chosen main menu option can be casteble to integer."""

        try:
            option = int(input("Choose an option: "))
            return option
        except:
            print("Wrong option!")
            return -1


    def menuPrinter(self) -> None:
        """Helper function for printing menu."""

        print("\n\n" + "*" * 27)
        print("\tCRYPT MENU")
        print("*" * 27)
        print("\n1. ENCRYPT \n2. DECRYPT \n3. EXIT\n")
        print("*" * 27, end="\n\n")


    def modePrinter(self, mode: str) -> None:
        """Helper function for printing mode menu."""

        print("\n" + "*" * 27)
        print(f"\t {mode.upper()}")
        print("*" * 27, end="\n\n")


    def mainMenu(self) -> int:
        """Main menu controller."""

        self.menuPrinter()
        while True:
            option = self.menuOptionCastable()

            if option == -1:
                continue

            validOption = self.menuChecker(option)
            if validOption == -1:
                continue

            return validOption            


    def run(self) -> None:
        """Main function."""

        cryptOption = self.mainMenu()

        if cryptOption == 1:
            self.modePrinter("encryption")

            text, spaceOpt = self.getText()
            key = self.getKey()

            crypted = self.encryptFoo(text, key, self._lowerCase, spaceOpt)

            print(f"Crypted Text: {crypted}\n")

            self.checkOS(crypted)
            
        else:
            self.modePrinter("decryption")

            text, spaceOpt = self.getText()
            key = self.getKey()

            decrypted = self.decryptFoo(text, key, self._lowerCase, spaceOpt)

            print(f"Derypted Text: {decrypted}\n")

            self.checkOS(decrypted)

        # Recursion part
        self.run()

if __name__ == "__main__":
    cryptor = EtTuBrute()
    cryptor.run()
