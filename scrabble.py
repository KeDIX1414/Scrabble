from tkinter import *


class Application(Frame):
    def create_widgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT.grid()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
