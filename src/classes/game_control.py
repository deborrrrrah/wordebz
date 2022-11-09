from .guess import Guess

class GameControl:
  def __init__(self):
    self.is_initialized = False
  
  def init(self, hidden_word: str):
    self.max_retry = 5
    self.retry_attempt = 0
    self.hidden_word = hidden_word.upper()
    self.is_guessed = False
    self.is_initialized = True
  
  def request_guess(self):
    guess_word = ""
    while len(guess_word) != len(self.hidden_word):
      guess_word = input("Guess: ").upper()
    return guess_word
  
  def run(self):
    if not self.is_initialized:
      print("Game is not initialized!")
      return
    while not self.is_guessed and self.retry_attempt < self.max_retry:
      guess_word = self.request_guess()
      guess = Guess(guess_word=guess_word, hidden_word=self.hidden_word)
      print(guess)
      if guess_word == self.hidden_word:
        self.is_guessed = True
      else:
        self.retry_attempt += 1
  