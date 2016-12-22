#########################################################################################
# This is the second menu screen that the user will first see. It is run on the boot via a
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
orange_font = (226, 180, 89)
white = (255, 255, 255)
red = (255, 0, 0)

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


def current_date_time():
    date_time = time.strftime("%a, %d %b %Y  %H:%M:%S", time.localtime()) # Uses the pi settings
    return date_time

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

def run_cmd(cmd):
    process = Popen(cmd.split(), stdout=PIPE)
    output = process.communicate()[0]
    return output

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
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1]) #  borrowed from pygame tutorial, heavily edited
    if 25 <= touch_pos[0] <= 245 and 105 <= touch_pos[1] <=160:
            button(1)
    if 265 <= touch_pos[0] <= 475 and 105 <= touch_pos[1] <=160:
            button(2)
    if 25 <= touch_pos[0] <= 245 and 180 <= touch_pos[1] <=235:
            button(3)
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

create_label(ip_addr_find(), 10, 30, 50, orange_font)
create_button("Crack WEP", 25, 105, 55, 210,orange_font)
create_button("Crack WPA", 265, 105, 55, 210, orange_font)
create_button("WPS", 25, 180, 55, 210, orange_font)
create_button("Jam Wi-fi", 265, 180, 55, 210, orange_font)
create_button("1", 25, 255, 55, 95, orange_font)
create_button("2", 145, 255, 55, 95, white)
create_button("3", 265, 255, 55, 95, orange_font)
create_button("4", 375, 255, 55, 95, orange_font)

def button(number):
    if number == 1:
        pygame.quit()
        subprocess.call(['/home/pi/pitftmenu/crack_wep.sh'])
        page=os.environ["MENUDIR"] + "listening_menu.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 2:
        subprocess.call(['/home/pi/pitftmenu/crack_wpa.sh'])
        pygame.quit()
        page=os.environ["MENUDIR"] + "listening_menu.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 3:
        subprocess.call(['/home/pi/pitftmenu/crack_wps.sh'])
        pygame.quit()
        page=os.environ["MENUDIR"] + "listening_menu.py"
        os.execvp("python", ["python", page])
        run_cmd("bash crack_wps.sh")
        sys.exit()

    if number == 4:
        subprocess.call(['/home/pi/pitftmenu/kill_wifi.sh'])
        subprocess.call(['/home/pi/pitftmenu/wifi_jammer.sh'])
        pygame.quit()
        page=os.environ["MENUDIR"] + "jamming_screen.py"
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
