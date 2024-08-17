#!/bin/sh

if [ "$1" == "on" ]; then
  sed --in-place "s/corner-radius = 0/corner-radius = 12/g" /home/seweryn/.config/picom/picom.conf
elif [ "$1" == "off" ]; then
  sed --in-place "s/corner-radius = 12/corner-radius = 0/g" /home/seweryn/.config/picom/picom.conf
else
  echo "Use on/off."
fi
