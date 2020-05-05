from epicAssets.menuCrap import *
from epicAssets.baseLevelAndPhysics import *
from dumbConstants import *

class ActualGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

        self.sfx = {"jump": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/jump.wav"),
                    "star": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/star.wav"),
                    "void": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/dropVoid.wav"),
                    "sting": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/beeSting.wav"),
                    "lost": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/levelLost.wav"),
                    "win": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/levelPass.wav"),
                    "spike": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/spike.wav"),
                    "level music": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/background.wav"),
                    "menu music": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/menu.wav"),
                    "burn": arcade.load_sound(str(Path(__file__).parent) + "/epicAssets/sounds/burn.wav")}
        self.currLevel = None

    def setup(self):
        self.menuView = MenuView()
        self.gameOver = GameOverView()
        self.levels = {i: Level(i) for i in range(1, 6 + 1)}
        self.game_over = False
        self.deathCause = None
        self.show_view(self.menuView)

def main():
    game = ActualGame()
    game.setup()
    arcade.run()

main()
