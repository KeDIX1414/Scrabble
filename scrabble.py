from tkinter import *
from place_word import *


class Application(Frame):
    # functions having to do with widgets
    def create_widgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT.grid()

    # respond to button presses
    def player_submission(self, word, position, direction):
        result = player_turn(game, word, position, direction)
        if result == "invalid word":
            pass
        elif result == "invalid placement":
            pass
        else:
            pass

    def computer_turn(self):
        pass

    def player_swap_tiles(self):
        pass

    def computer_swap_tiles(self):
        pass

    def get_hint(self):
        pass

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.game = Game()
        set_dictionary(Dictionary["hello", "goodbye"])
        set_game(self.game)
        self.grid()
        self.create_widgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
