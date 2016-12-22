#########################################################################################
# This is the third menu screen that the user will first see. It is run on the boot via a
# shell script "menu_start.sh" in the /.profile.
#########################################################################################
#!/usr/bin/env python
import sys, os, subprocess, time, pygame, socket
from pygame.locals import *
from subprocess import *
from pygame.locals import *
from subprocess import *

grey_background = (60, 61, 60)
grey_border = (65, 57, 57)
orange_font= (226, 180, 89)
white = (255, 255, 255)

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

pygame.display.init()
pygame.font.init()
pygame.mouse.set_visible(0)

size_width = 480
size_height = 320
screen = pygame.display.set_mode((size_width,size_height))
screen.fill(grey_background)
pygame.draw.rect(screen, white, (0,0,479,319),8)
pygame.draw.rect(screen, white, (2,2,479-4,319-4),2)


def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output


def get_temp(): #uses rpi
    command = "vcgencmd measure_temp"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    temp = output[5:-1]
    return temp


def get_volts(): #uses rpi
    command = "vcgencmd measure_volts"
    process = Popen(command.split(), stdout=PIPE)
    output = process.communicate()[0]
    volts = output[5:-1]
    return volts


def create_button(text, xpo, ypo, height, width, colour):
    pygame.draw.rect(screen, white, (xpo-10,ypo-10,width,height),3)
    pygame.draw.rect(screen, white, (xpo-9,ypo-9,width-1,height-1),1)
    pygame.draw.rect(screen, white, (xpo-8,ypo-8,width-2,height-2),1)
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


def create_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


def touch_input():
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    if 265 <= touch_pos[0] <= 475 and 180 <= touch_pos[1] <=235:
            button(4)
    if 25 <= touch_pos[0] <= 125 and 255 <= touch_pos[1] <=310:
            button(5)
    if 135 <= touch_pos[0] <= 245 and 255 <= touch_pos[1] <=310:
            button(6)
    if 255 <= touch_pos[0] <= 355 and 255 <= touch_pos[1] <=310:
            button(7)
    if 365 <= touch_pos[0] <= 475 and 255 <= touch_pos[1] <=310:
            button(8)

create_label("Volts", 10, 30, 50, white)
create_label("Temp", 10, 60, 50, white)
create_label(get_volts(), 120, 30, 50, orange_font)
create_label(get_temp(), 120, 60, 50, orange_font)
create_button("Refresh", 265, 180, 55, 210, orange_font)
create_button("1", 25, 255, 55, 95, orange_font)
create_button("2", 145, 255, 55, 95, orange_font)
create_button("3", 265, 255, 55, 95, white)
create_button("4", 375, 255, 55, 95, orange_font)


def button(number):

    if number == 4:
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu3.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 5:
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu1.py"
        os.execvp("python", ["python", page])
        run_cmd("bash crack_wps.sh")
        sys.exit()

    if number == 6:
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu2.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 7:
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu3.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        pygame.quit()
        page=os.environ["MENUDIR"] + "cracking_menu4.py"
        os.execvp("python", ["python", page])
        sys.exit()


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
