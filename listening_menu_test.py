#!/usr/bin/env python
import sys, os, subprocess, pygame, socket
from pygame.locals import *
from subprocess import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

grey_background = (60, 61, 60)
grey_border = (65, 57, 57)
orange_font= (226, 180, 89)
white = (255, 255, 255)
red = (255,   0,   0)

pygame.font.init()
pygame.display.init()
pygame.mouse.set_visible(0)
size_width = 480
size_height = 320
screen = pygame.display.set_mode((size_width,size_height))
screen.fill(grey_background)
pygame.draw.rect(screen, white, (0,0,479,319),8)
pygame.draw.rect(screen, white, (2,2,479-4,319-4),2)


def mac_results():
    text_file = open("/home/pi/pitftmenu/crackedtest.csv", "r")
    for line in text_file:
        fields = line.split(",")
    wi_mac = fields[0]
    if os.path.exists("/home/pi/pitftmenu/crackedtest.csv"):
        return ("Mac - "  + wi_mac)
    else:
        return ("Network being cracked, please refresh")


def sec_type():
    text_file = open("/home/pi/pitftmenu/crackedtest.csv", "r")
    for line in text_file:
        fields = line.split(",")
    wi_security = fields[1]
    if os.path.exists("/home/pi/pitftmenu/cracked.csv"):
        return ("Security Level - " + wi_security)
    else:
        return ("Network being cracked, please refresh")


def ac_pass_name():
    text_file = open("/home/pi/pitftmenu/crackedtest.csv", "r")
    for line in text_file:
        fields = line.split(",")
    ap_name = fields[2]
    if os.path.exists("/home/pi/pitftmenu/crackedtest.csv"):
        return ("Name - " + ap_name)
    else:
        return ("Network being cracked, please refresh")


def ap_pass():
    text_file = open("/home/pi/pitftmenu/crackedtest.csv", "r")
    for line in text_file:
        fields = line.split(",")
    wi_pass = fields[3]
    if os.path.exists("/home/pi/pitftmenu/crackedtest.csv"):
        return ("Password - " + wi_pass)
    else:
        return ("Network being cracked, please refresh")


def ip_addr_find():
    ip_status = "Offline"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('<broadcast>', 0))
        ip_status="Connected IP: " + s.getsockname()[0]
    except Exception:
        pass
    return ip_status


def create_label(text, xpo, ypo, fontsize, colour):
    font=pygame.font.Font(None,fontsize)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))


def create_italic_label(text, xpo, ypo, fontsize, colour):
    font = pygame.font.Font(None, fontsize)
    label = font.render(str(text), 1, (colour))
    screen.blit(label, (xpo, ypo))


def create_button(text, xpo, ypo, height, width, colour):
    pygame.draw.rect(screen, white, (xpo-10,ypo-10,width,height),3)
    pygame.draw.rect(screen, white, (xpo-9,ypo-9,width-1,height-1),1)
    pygame.draw.rect(screen, white, (xpo-8,ypo-8,width-2,height-2),1)
    font=pygame.font.Font(None,42)
    label=font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))



def touch_input():
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    if 30 <= touch_pos[0] <= 240 and 190 <= touch_pos[1] <=235:
            button(1)
    if 260 <= touch_pos[0] <= 470 and 190 <= touch_pos[1] <=235:
            button(2)
    if 30 <= touch_pos[0] <= 240 and 255 <= touch_pos[1] <=310:
            button(3)
    if 260 <= touch_pos[0] <= 470 and 255 <= touch_pos[1] <=310:
            button(4)


def button(number):
    if number == 1:
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu_screenoff.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 2:
        pygame.quit()
        subprocess.call(['/home/pi/pitftmenu/file_transfer.sh'])
        page=os.environ["MENUDIR"] + "first_screen_option.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 3:
        # first button
        pygame.quit()
        subprocess.call(['/home/pi/pitftmenu/del_cracked.sh'])
        page=os.environ["MENUDIR"] + "listening_menu.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 4:
        pygame.quit()
        sys.exit()

create_button("Hide", 30, 190, 55, 210, orange_font)
create_button("Send", 260, 190, 55, 210, orange_font)
create_button("Delete", 30, 255, 55, 210, orange_font)
create_button("Exit", 260, 255, 55, 210, orange_font)
create_label(ip_addr_find(), 40, 20, 45, orange_font)
create_label(mac_results(), 120, 60, 25, white)
create_label(sec_type(), 120, 85, 25, white)
create_label(ac_pass_name(), 120, 110, 25, white)
create_label(ap_pass(), 120, 135, 25, white)


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
