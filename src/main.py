from classes.guess import Guess
from colorama import reinit

if __name__ == "__main__":
  gs = [
    Guess("ABCDE", "AAEAA"),
    Guess("AABCD", "AAAAA")
  ]
  for g in gs:
    reinit()
    print(g)