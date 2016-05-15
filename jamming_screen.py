#!/usr/bin/env python
import sys, os, subprocess, time, pygame, socket
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

grey_background = (60, 61, 60)
grey_border = (65, 57, 57)
orange_font = (226, 180, 89)
white = (255, 255, 255)

pygame.font.init()  # init separate, so doesnt cause errors.
pygame.display.init()
pygame.mouse.set_visible(0)

# set size of the screen, making them variables, for changing at a later date. 2.8 inch versions are also available
size_width = 480
size_height = 320
screen = pygame.display.set_mode((size_width, size_height))
# background colour fill
screen.fill(grey_background)
# border
pygame.draw.rect(screen, white, (0, 0, 479, 319), 8)
pygame.draw.rect(screen, white, (2, 2, 479-4, 319-4), 2)

# text but not button
def create_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# italic text
def create_italic_label(text, xpo, ypo, fontsize, colour):
    font = pygame.font.Font(None, fontsize)
    label = font.render(str(text), 1, (colour))
    screen.blit(label, (xpo, ypo))

#def countdown(n):
#     while n > 0:
#         n = 30
#         return (n)
#         return("Finished")


# define function for printing text in a specific place with a specific width and height with a specific colour and border
def create_button(text, xpo, ypo, height, width, colour):
    pygame.draw.rect(screen,white, (xpo-10,ypo-10,width,height),3)
    pygame.draw.rect(screen, white, (xpo-9,ypo-9,width-1,height-1),1)
    pygame.draw.rect(screen, white, (xpo-8,ypo-8,width-2,height-2),1)
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))

# allows running of basic commands in the python script rather than making a whole bash script
def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

def touch_input():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1]) #  borrowed from pygame tutorial, heavily edited
    # button 1 event starting top left
    if 30 <= touch_pos[0] <= 240 and 255 <= touch_pos[1] <=310:
            button(3)
    if 260 <= touch_pos[0] <= 470 and 255 <= touch_pos[1] <=310:
            button(4)

def button(number):
    if number == 3:
        # first button
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu1.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 4:
        pygame.quit()
        sys.exit()

create_italic_label("Wifi Being Disrupted", 80, 30, 45, orange_font)
create_label("Time, 30 seconds", 120, 100, 40, orange_font)
create_button("Menu", 30, 255, 55, 210, orange_font)
create_button("Exit", 260, 255, 55, 210, orange_font)


# touch screen loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
            touch_input()

        # exits even if touch screen errors
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
    pygame.display.update()
    time.sleep(0.1)
