from typing import List

class Word:
  def __init__(self, word_chars: List[str]):
    self.word_chars = word_chars
    
  def __eq__(self, other):
    if len(self.word_chars) != len(other):
      return False
    for i in range(len(self.word_chars)):
      if self.word_chars[i] != other[i]:
        return False
    return True
  
  def contain(self, char):
    return char in self.word_chars