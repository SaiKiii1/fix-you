import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("High up above, or down below", 0.12),
        ("When you're too in love to let it go", 0.08),
        ("But if you never try, you'll never know", 0.08),
        ("Just what you're worth", 0.10),
        ("Lights will guide you home", 0.16),
        ("And ignite your bones", 0.24),
        ("And I will try to fix you", 0.19),
        (" ", 150),
    ]

    delays = [3.5, 3.5, 2.5, 7.8, 2.3, 2.5, 0.5, 3, 3]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()