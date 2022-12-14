from mainframe import MainFrame
from player import Player
from gamedata import GameData

if __name__ == '__main__':
    gd = GameData()
    gd.print()
    print('')
    player = Player()
    player.print()
    print('-------------------')
    player.loadfile(gd.last_game())
    player.print()
    app = MainFrame()
    app.mainloop()

