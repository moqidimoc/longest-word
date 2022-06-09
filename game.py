# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string

class Game:

    # When we initialize the game, we create the grid
    def __init__(self):
        self.grid = self.random_grid()

    # We generate 9 random letters and append them to the grid
    def random_grid(self):
        grid = []

        for _ in range(9):
            letter = random.choice(string.ascii_letters).upper()
            grid.append(letter)

        return grid

    # This function will test if the word has letter from the grid
    def is_valid(self, word):
        answer  = False

        if not word:
            return answer

        letters = self.grid.copy()
        for letter in word:
            if letter not in letters:
                answer = False
                break
            answer = True

        return answer
