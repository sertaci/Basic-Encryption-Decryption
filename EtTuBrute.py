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
version ='i.314.271.161.662'
---------------------------------------------------------------------------
"""


import string
import re
import subprocess
import platform


class EtTuBrute():
    _keyList = []
    _lowerCase = []
    def __init__(self):
        self._keyList = [314, 271, 161, 662]
        self._lowerCase = list(string.ascii_lowercase)


    def menuPrinter(self):
        """Helper function for printing menu."""

        print("\n\n" + "*" * 27)
        print("\tCRYPT MENU")
        print("*" * 27)
        print("\n1. ENCRYPT \n2. DECRYPT \n3. EXIT\n")
        print("*" * 27, end="\n\n")


    def modePrinter(self, mode: str):
        """Helper function for printing mode menu."""

        print("\n" + "*" * 27)
        print(f"\t {mode.upper()}")
        print("*" * 27, end="\n\n")


    def menuOptionCast(self) -> int:
        """Check whether the chosen main menu option can be casteble to integer."""

        try:
            option = int(input("Choose an option: "))
            return option
        except:
            print("Wrong option!")
            return -1


    def menuChecker(self, option: int) -> int:
        """Check if the option is in the list."""

        if option not in [1, 2, 3]:
            print("Wrong option!")
            return -1

        elif option == 3:
            exit()

        # Returning the crypt or decrypt mode (1 or 2)
        else:
            return option


    def mainMenu(self) -> int:
        """Main menu controller"""

        self.menuPrinter()
        while True:
            option = self.menuOptionCast()

            if option == -1:
                continue

            validOption = self.menuChecker(option)
            if validOption == -1:
                continue

            return validOption


    def encryptFoo(self, text: str, key: int, lowerCase: list) -> str:
        """Crypting function. Basically it uses caesar cipher method.
        If it exceeds the lowercase alphabet, basically it makes some modulo operation.
        """

        crypted = ""

        for i in text:
            a = ord(i) + (key % 26)
            if a > 122:
                crypted += lowerCase[a % 122-1]

            else:
                crypted += chr(a)

        return crypted


    def decryptFoo(self, text: str, key: int, lowerCase: list) -> str:
        """Derypting function. Reverse of the encrypt function"""

        decrypted = ""

        for i in text:
            a = ord(i) - (key % 26)

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


    def cleanText(self, text: str) -> str:
        """Convert input text to lowercase characters."""

        text = re.sub("[^a-zA-Z]", "", text)
        text = text.lower().strip()

        return text


    def getText(self) -> str:
        """Getting the input text and clean it for the encryption or decryption."""

        while True:
            text = input(
                "Enter the text as adjacent lowercase characters (or it will be lowercased and truncated): "
            )
            text = self.cleanText(text)

            textConfirmation = input(f"\nText will be: {text}\nIs it okay? (y/n): ")
            print("")
            if textConfirmation == "y" or textConfirmation == "\n":
                return text

            noChoice = self.noChoiceAction()
            if noChoice == -1 or noChoice == -2:
                noChoice = self.noChoiceAction()

            elif noChoice == 1:
                continue
            else:
                self.main()


    def getKey(self) -> int:
        """Getting the proper key until the proper key is entered."""

        key = int(input("Enter the key: "))
        
        while key not in self._keyList:
            print("Wrong key!")
            key = int(input("Re-enter the key: "))

        print("")
        return key


    def copyClipBoard(self, text):
        """Copy result to the clipboard."""

        command = "echo " + text + "|clip"
        return subprocess.check_call(command, shell=True)


    def main(self):
        """Main function for processing all the functions"""

        cryptOption = self.mainMenu()

        if cryptOption == 1:
            self.modePrinter("encryption")

            text = self.getText()
            key = self.getKey()

            crypted = self.encryptFoo(text, key, self._lowerCase)

            print(f"Crypted Text: {crypted}\n")
            # If the system is Windows, call the unique win command executer function to copy clipboard 
            if platform.system() == "Windows":
                input(
                    "Press enter to copy crypted text to the clipboard and go to the menu."
                )
                self.copyClipBoard(crypted)
            else:
                input("Press enter to go to the menu ")
            self.main()

        else:
            self.modePrinter("decryption")

            text = self.getText()
            key = self.getKey()

            decrypted = self.decryptFoo(text, key, self._lowerCase)

            print(f"Derypted Text: {decrypted}\n")
            # If the system is Windows, call the unique win command executer function to copy clipboard 
            if platform.system() == "Windows":
                input(
                    "Press enter to copy decrypted text to the clipboard and go to the menu."
                )
                self.copyClipBoard(decrypted)
            else:
                input("Press enter to go to the menu ")
            self.main()


if __name__ == "__main__":
    cryptor = EtTuBrute()
    cryptor.main()
