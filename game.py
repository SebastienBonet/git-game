# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

class Game:
    def __init__(self):
        self.grid = []
        letters = [i for i in string.ascii_uppercase]
        self.grid = random.sample(letters, 9)
        #print(self.grid)

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
            #return True

        return self.__checkdico(word)


    def __checkdico(self, word):
        req = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = req.json()
        return response['found']
