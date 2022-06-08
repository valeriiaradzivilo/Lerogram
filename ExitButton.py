from tkinter import Button, messagebox


class ExitButton(Button):
    def __init__(self, window):
        self.window = window
        Button.__init__(self)
        self['bg'] = 'red'
        self['text'] = "X"
        self['width'] = 5
        self['height'] = 2
        self['command'] = lambda: ExitButton.exit_message(self)
        self.place(x=610, y=20)

    # message that appears after you press 'Exit'
    def exit_message(self):
        msgBox = messagebox.askquestion("Exit", "Do you want to exit the game?")
        if msgBox == 'yes':
            # exit the game
            print("Exit")
            self.window.destroy()
            self.window.replay.append('n')

        else:
            # close message
            print("No exit")
