import curses as cur
from curses import wrapper
import time
import random
import os
import sys


# def counter(stdscr):
#     timeOut = 120  # seconds which means 2 minutes solving time

#     for timer in range(0, timeOut, 1):
#         sys.stdout.write("\r")
#         sys.stdout.write("{:2d}".format(timer))
#         sys.stdout.flush()
#         time.sleep(1)


def main(stdscr):
    # Create and display scramble
    moves = ["R", "R'", "R2", "L", "L'", "L2", "U", "U'", "U2", "D",
             "D'", "D2", "B", "B'", "B2", "F", "F'", "F2"]

    scramble = []
    prevIndex = -1
    while len(scramble) < 21:
        index = random.randrange(len(moves))

        # check that no two movements are next to each other
        if (index/3) != (prevIndex/3):
            scramble.append(moves[index])
            prevIndex = index

    createdScramble = "".join(scramble)

    # Calling stuff for showing on the screen
    stdscr.clear()
    stdscr.addstr("Rubics cube timer!")
    stdscr.addstr("\nThere is mixing introductions under below")

    stdscr.addstr(f"\n{createdScramble}\n")

    stdscr.addstr("\nPress any key to start the timer\n")
    stdscr.refresh()
    stdscr.getkey()

    count = 10
    for x in range(0, 10):
        stdscr.addstr(str(count))
        stdscr.refresh()
        time.sleep(1)
        count = count-1
        stdscr.clear()

    while True:
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
