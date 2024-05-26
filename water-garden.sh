#!/bin/bash
/usr/local/bin/kasa --host 192.168.1.193 on --name 'garden pump'
echo "Watering started"
sleep 15m
/usr/local/bin/kasa --host 192.168.1.193 off --name 'garden pump'
echo "Watering complete"

