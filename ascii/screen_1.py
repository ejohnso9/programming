#!/usr/bin/env python

from asciimatics.screen import Screen
from time import sleep

def demo(screen):
    screen.print_at('Hello, world!', 20, 20)
    screen.refresh()
    sleep(3)

Screen.wrapper(demo)

