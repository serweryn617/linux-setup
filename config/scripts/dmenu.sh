#!/bin/bash

green1="#00cc52"
pink1="#d849ff"
pink2="#c23ee6"
darker_gray="#383838"
bg_dark="#181818"
text="#cccccc"
white="#ffffff"

dmenu_custom() {
  dmenu \
  -c -h 24 -l 10 -bw 2 -fn 'GitLab Mono' \
  -nb $bg_dark -nf $text -sb $darker_gray -sf $white \
  -nhf $pink2 -shf $pink1 -nhb $bg_dark -shb $darker_gray -bc $green1 -i
}

dmenu_run_custom() {
  dmenu_run \
  -c -h 24 -l 10 -bw 2 -fn 'GitLab Mono' \
  -nb $bg_dark -nf $text -sb $darker_gray -sf $white \
  -nhf $pink2 -shf $pink1 -nhb $bg_dark -shb $darker_gray -bc $green1 -i
}