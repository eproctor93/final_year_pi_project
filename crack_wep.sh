#!/usr/bin/env bash
sudo airmon-ng check kill
sudo airmon-ng start wlan2
wait 5s
sudo python /home/pi/pitftmenu/wifite.py -all -wept 10 &

