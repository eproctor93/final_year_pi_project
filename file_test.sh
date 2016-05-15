#!/bin/bash
if [ -f /home/pi/pitftmenu/first_screen_option.py ]; then
    echo "FOUND /first_screen_option.py"
fi
if [ ! -f /home/pi/pitftmenu/first_screen_option.py ]; then
    echo "NOT FOUND /first_screen_option.py"
fi

if [ -f /home/pi/pitftmenu/cracking_menu1.py ]; then
    echo "FOUND /cracking_menu1.py"
fi
if [ ! -f /home/pi/pitftmenu/cracking_menu1.py ]; then
    echo "NOT FOUND /cracking_menu1.py"
fi

if [ -f /home/pi/pitftmenu/cracking_menu2.py ]; then
    echo "FOUND /cracking_menu2.py"
fi
if [ ! -f /home/pi/pitftmenu/cracking_menu2.py ]; then
    echo "NOT FOUND /cracking_menu2.py"
fi

if [ -f /home/pi/pitftmenu/cracking_menu3.py ]; then
    echo "FOUND /cracking_menu3.py"
fi
if [ ! -f /home/pi/pitftmenu/cracking_menu3.py ]; then
    echo "NOT FOUND /cracking_menu3.py"
fi

if [ -f /home/pi/pitftmenu/cracking_menu4.py ]; then
    echo "FOUND /cracking_menu4.py"
fi
if [ ! -f /home/pi/pitftmenu/cracking_menu4.py ]; then
    echo "NOT FOUND /cracking_menu4.py"
fi

if [ -f /home/pi/pitftmenu/jamming_screen.py ]; then
    echo "FOUND /jamming_screen.py"
fi
if [ ! -f /home/pi/pitftmenu/jamming_screen.py ]; then
    echo "NOT FOUND /jamming_screen.py"
fi

if [ -f /home/pi/pitftmenu/listening_mode.py ]; then
    echo "FOUND /listening_mode.py"
fi
if [ ! -f /home/pi/pitftmenu/listening_mode.py ]; then
    echo "NOT FOUND /listening_mode.py"
fi

echo -e "Tests \e[5mFinished\e[25m"



FILE1= /home/pi/pitftmenu/first_screen_option.py
FILE2= /home/pi/pitftmenu/cracking_menu1.py
FILE3= /home/pi/pitftmenu/cracking_menu2.py
FILE4= /home/pi/pitftmenu/cracking_menu3.py
FILE5= /home/pi/pitftmenu/cracking_menu4.py
FILE6= /home/pi/pitftmenu/listening_mode.py
FILE7= /home/pi/pitftmenu/listening_menu.py
