#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import locale
import random
import time


participants = [
    # Lista uczestników zarejestrowanych
]


def winner(stdscr):
    '''Show a random participant from the list,
    stop when a button is pressed.'''

    stdscr.nodelay(True)

    max_y, max_x = stdscr.getmaxyx()
    winner = 'The winner is: '
    pos_x = max_x / 2 + len(winner) / 2
    pos_y = max_y / 2


    stdscr.addstr(pos_y, pos_x - len(winner), winner)

    while stdscr.getch() == curses.ERR:
        the_chosen_one = random.choice(participants).encode('utf-8')

        # Clear the place for the winners name
        stdscr.hline(pos_y, pos_x, ' ', max_x - pos_x)

        # Print the name
        stdscr.addstr(pos_y, pos_x, the_chosen_one)

        stdscr.refresh()
        time.sleep(.005)

    stdscr.nodelay(False)
    stdscr.hline(max_y - 2, 0, '-', max_x)
    stdscr.addstr(max_y - 1, 0, 'Press enter to finish...')

    while True:
        inpt = stdscr.getch()

        if inpt == ord('\n') or inpt == curses.KEY_ENTER:
            break


if __name__ == '__main__':
    if not participants:
        print 'No participants provided. Finishing.'
    else:
        locale.setlocale(locale.LC_ALL, "")
        curses.wrapper(winner)
