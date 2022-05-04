import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any key to begin")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM: {wpm}')
    for i, letter in enumerate(current):
        correct_letter = target[i]
        color = curses.color_pair(1)
        if letter != correct_letter:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, letter, color)

def load_text():
    with open("tutorial_sample_text.txt", 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()
        # strip() - removes any leading or trailing white space character;  /n - whitespace character 
    
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0 
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60))/5)
        # dividing by  5; assuming average words is 5 characters long

        stdscr.clear()  
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
            # this is acting as blocker, so insert try-except block to get around it
        except:
            continue
    
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif ord(key) == 27:
            break
        elif len(current_text) < len(target_text):
            current_text.append(key)
        
        

    

def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the test! Press any key to continue..")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)