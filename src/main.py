from classes.game_control import GameControl
from colorama import reinit

if __name__ == "__main__":
  gc = GameControl()
  gc.init()
  gc.run()