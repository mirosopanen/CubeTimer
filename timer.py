import curses
from curses import wrapper
import time
import random
import os
import sys


def startScreen(stdscr):
    stdscr.clear()
    stdscr.addstr("Rubics cube timer!")
    stdscr.addstr("\nPress any key to start the timer")
    stdscr.refresh()
    stdscr.getkey()


def counter(stdscr):
    pass


def createShufflingScramble(stdscr, moves, createdScramble):
    scramble = []
    prevIndex = -1
    while len(scramble) < 21:
        index = random.randrange(len(moves))

        # check that no two movements are next to each other
        if (index/3) != (prevIndex/3):
            scramble.append(moves[index])
            prevIndex = index

    createdScramble = "".join(scramble)


def main(stdscr):
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D",
             "D'", "D2", "B", "B'", "B2", "F", "F'", "F2"]

    startScreen(stdscr)


wrapper(main)
# timeOut = 120  # seconds which means 2 minutes solving time

# for timer in range(0, timeOut, 1):
#     sys.stdout.write("\r")
#     sys.stdout.write("{:2d}".format(timer))
#     sys.stdout.flush()
#     time.sleep(1)
