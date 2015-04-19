#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import locale
import random


fontsize = 50

participants = [
    # Lista uczestników zarejestrowanych
]


class WinnerGUI(object):

    def __init__(self, fontsize):
        self.root = tk.Tk()
        self.root.state('zoomed')
        self.root.title('Winner generator')
        self.stop = False
        self.fontsize = fontsize
        self.bind_events()

    def bind_events(self):
        self.root.bind_all('<Key>', self.keypress)
        self.root.bind('<Button-1>', self.keypress)

    def keypress(self, key):
        self.stop = True

    def show(self):
        the_chosen_one = tk.StringVar()
        
        self.root.configure(background='white')
        frame = tk.Frame(self.root)
        
        winner = tk.Label(frame, text='The winner is: ',
                          font=(None, self.fontsize))
        winner.configure(background='white')
        winner.pack(fill=tk.X)
        
        label = tk.Label(frame, textvariable=the_chosen_one,
                         font=(None, self.fontsize))
        label.configure(background='white')
        label.pack(fill=tk.X)

        frame.configure(background='white')
        frame.pack(expand=tk.YES)
        self.randomize_winner(the_chosen_one)
        self.root.mainloop()

    def randomize_winner(self, the_chosen_one):
        the_chosen_one.set(random.choice(participants).encode('utf-8'))

        if not self.stop:
            self.root.after(5, self.randomize_winner, the_chosen_one)


if __name__ == '__main__':
    if not participants:
        print 'No participants provided. Finishing.'
    else:
        locale.setlocale(locale.LC_ALL, "")
        window = WinnerGUI(fontsize)
        window.show()
