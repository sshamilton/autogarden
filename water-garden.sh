#!/bin/bash
/home/stephen/venv/bin/kasa --host 192.168.1.98 on --name 'garden pump'
echo "Watering started"
sleep 15m
/home/stephen/venv/bin/kasa --host 192.168.1.98 off --name 'garden pump'
echo "Watering complete"

