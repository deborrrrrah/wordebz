from typing import List
from colorama import Fore, Back

from .word import Word

class Guess:
  def __init__(self, guess_word: Word, hidden_word: Word):
    self.guess_word = guess_word
    self.hidden_word = hidden_word
  
  @property
  def correct_char(self):
    return Fore.WHITE + Back.GREEN
  
  @property
  def half_guessed_char(self):
    return Fore.WHITE + Back.YELLOW
  
  @property
  def wrong_char(self):
    return Fore.WHITE + Back.BLACK
  
  def __str__(self):
    gw_length = len(self.guess_word)
    hw_length = len(self.hidden_word)
    if gw_length != hw_length:
      return f"Error: guess word length {gw_length} is different with hidden word length {hw_length}"
    display_chars = []
    for idx in range(gw_length):
      gw_char = self.guess_word[idx]
      if self.hidden_word[idx] == gw_char:
        display_chars.append(self.correct_char + gw_char)
      elif gw_char in self.hidden_word:
        display_chars.append(self.half_guessed_char + gw_char)
      else:
        display_chars.append(self.wrong_char + gw_char)
    return "".join(display_chars)
