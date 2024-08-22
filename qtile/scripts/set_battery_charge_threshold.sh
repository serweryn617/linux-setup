#!/bin/bash

LIMIT=$(cat /sys/class/power_supply/BAT0/charge_control_end_threshold)

echo "Change current battery charge threshold ($LIMIT%) to $1%?"
echo "This setting will be reset to 80% on reboot."
echo
echo $1 | sudo tee /sys/class/power_supply/BAT0/charge_control_end_threshold > /dev/null

RES=$?
echo

if [ $RES -ne 0 ]; then
    echo "Something went wrong!"
else
    LIMIT=$(cat /sys/class/power_supply/BAT0/charge_control_end_threshold)
    echo "New charge limit set to $LIMIT%!"
fi

echo "Press Enter to exit..."

read
