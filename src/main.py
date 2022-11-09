import random
from os import system
from colorama import reinit
from classes.game_control import GameControl


def select_hidden_word():
  with open("hidden_words.txt", "r") as f:
    words = f.readlines()
    hidden_word = random.choice(words).strip()
    return hidden_word


def clear_screen():
  _ = system("clear")

if __name__ == "__main__":
  clear_screen()
  print("Welcome to Make Your Own Wordle!")
  gc = GameControl()
  hidden_word = select_hidden_word()
  gc.init(hidden_word=hidden_word)
  gc.run()