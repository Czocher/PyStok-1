#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import locale
import random


# Rozmiar fontu, ustaw tak, by mieściło się na ekranie
fontsize = 50

participants = [
    # Lista uczestników zarejestrowanych
]


class WinnerGUI(tk.Frame):

    def __init__(self, master=None, fontsize=50):
        tk.Frame.__init__(self, master)
        master.configure(background='black')

        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("{}x{}+0+0".format(w, h))

        self.stop = False
        self.fontsize = fontsize
        self.bind_events()
        self.create_widgets()

    def bind_events(self):
        self.bind_all('<Key>', self.keypress)
        self.bind_all('<Button-1>', self.keypress)
        self.bind_all('<Escape>', self.escapepress)

    def keypress(self, key):
        self.stop = True

    def escapepress(self, key):
        if not self.stop:
            self.stop = True
        else:
            self.quit()

    def create_widgets(self):
        the_chosen_one = tk.StringVar()

        winner = tk.Label(self, text='The winner is: ',
                          font=(None, self.fontsize))
        winner.configure(background='black', foreground='white')
        winner.pack(fill=tk.X)

        label = tk.Label(self, textvariable=the_chosen_one,
                         font=(None, self.fontsize))
        label.configure(background='black', foreground='white')
        label.pack(fill=tk.X)

        self.configure(background='black')
        self.pack(expand=tk.YES, fill=tk.X)

        self.randomize_winner(the_chosen_one)

    def randomize_winner(self, the_chosen_one):
        the_chosen_one.set(random.choice(participants))

        if not self.stop:
            self.after(5, self.randomize_winner, the_chosen_one)


if __name__ == '__main__':
    if not participants:
        print 'No participants provided. Finishing.'
    else:
        locale.setlocale(locale.LC_ALL, "")
        root = tk.Tk()
        root.title('Winner generator')
        window = WinnerGUI(root, fontsize)
        window.mainloop()
        root.destroy()
