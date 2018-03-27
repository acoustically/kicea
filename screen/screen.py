import sys
import os

class Screen:
    def clear():
        Screen.print("\033[2J")
        Screen.print("\033[0;0H")

    def print(code):
        sys.stdout.write(code)
        sys.stdout.flush()
  
    def size():
        return os.popen('stty size', 'r').read().split()
    
