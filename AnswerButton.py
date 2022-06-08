from tkinter import messagebox
from CheckButton import CheckButton


class AnswerButton(CheckButton):
    def __init__(self, yel_coord):
        self.yel_coord = yel_coord
        super().__init__()
        self['text'] = "Answer"
        self['command'] = lambda: AnswerButton.show_answer(self)
        self.place(x=310, y=530)

    def show_answer(self):
        text_answ = ""
        text_answ += "Answer: \n"
        text_answ += "(column: row1, row2,...)\n"
        text_answ += "  Yellow boxes:\n"
        for i in range(15):
            text_answ += str(i + 1) + ": "
            for j in range(15):
                if (i, j, 'y') in self.yel_coord and j != 15:
                    text_answ += str(j + 1) + " "
            text_answ += '\n'
        text_answ += "    Back boxes:\n"
        for i in range(15):
            text_answ += str(i + 1) + ": "
            for j in range(15):
                if (i, j, 'y') not in self.yel_coord and j != 15:
                    text_answ += str(j + 1) + " "
            text_answ += '\n'

        messagebox.showinfo("Answer", text_answ)
