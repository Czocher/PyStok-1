# -*- coding: utf-8 -*-

import thread
import time
import random
import sys
import os


participants = [
    # Lista uczestników zarejestrowanych
]


def input_thread(L):
    raw_input()

    L.append(None)


def the_winer_is():
    L = []

    thread.start_new_thread(input_thread, (L,))

    while 1:
        time.sleep(.005)
       
        os.system('clear')

        if L:
            print(u"The winer is:\n\n\t{0}\n".format(random.choice(participants)))

            break

        print(random.choice(participants))


if __name__ == '__main__':
    the_winer_is()
