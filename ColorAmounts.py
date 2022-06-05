from tkinter import Label


class ColorAmounts(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['bg'] = 'white'
        self['width'] = 2
        self['height'] = 1
