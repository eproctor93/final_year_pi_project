#!/usr/bin/env python
import sys, os, subprocess, time, pygame, socket
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

grey_background = (60, 61, 60)
grey_border = (65, 57, 57)
orange_font= (226, 180, 89)
white = (255, 255, 255)

pygame.font.init()
pygame.display.init()
pygame.mouse.set_visible(0)
# set size of the screen, making them variables, for changing at a later date. 2.8 inch versions are also avaible.
size_width = 480
size_height = 320
screen = pygame.display.set_mode((size_width,size_height))
screen.fill(grey_background)
pygame.draw.rect(screen, white, (0,0,479,319),8)
pygame.draw.rect(screen, white, (2,2,479-4,319-4),2)


def create_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


def create_italic_label(text, xpo, ypo, fontsize, colour):
    font = pygame.font.Font(None, fontsize)
    label = font.render(str(text), 1, (colour))
    screen.blit(label, (xpo, ypo))


def create_button(text, xpo, ypo, height, width, colour):
    pygame.draw.rect(screen,white, (xpo-10,ypo-10,width,height),3)
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


def touch_input():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    # button 1 event starting top left
    if 25 <= touch_pos[0] <= 245 and 180 <= touch_pos[1] <=235:
            button(1)
    # button 2 event
    if 265 <= touch_pos[0] <= 475 and 180 <= touch_pos[1] <=235:
            button(2)

def button(number):
    if number == 1:
        # first button
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu1.py"
        os.execvp("python", ["python", page])
        sys.exit()
    if number == 2:
        # second button
        pygame.quit()
        page=os.environ["MENUDIR"] + "listening_mode.py"
        os.execvp("python", ["python", page])
        sys.exit()


create_italic_label("Wireless Pi Cracking", 80, 30, 45, orange_font)
create_label("Only continue if you have the permission", 20, 80, 30, orange_font)
create_label("of the local wireless networks", 20, 100, 30, orange_font)
create_button("Cracking", 25, 180, 55, 210, orange_font)
create_button("Listening", 265, 180, 55, 210, orange_font)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            touch_input()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
    time.sleep(0.1)
