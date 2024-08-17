import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([script])


@hook.subscribe.client_new
def display_password_terminal(client):
    if client.name == 'password-terminal':
        client.set_size_floating(800, 300)


@hook.subscribe.client_new
def display_info_terminal(client):
    if client.name == 'info-terminal':
        client.set_size_floating(800, 800)


# PICOM DBUS

# dbus-send --dest=com.github.chjj.compton._0 / com.github.chjj.compton.win_set

# #!/bin/bash
# setshadow(){
#     dpy=$(printf "$DISPLAY" | tr -c '[:alnum:]' _)
#     for id in $(bspc query -N -n .window); do
#         dbus-send --print-reply \
#             --dest=com.github.chjj.compton.${dpy} / com.github.chjj.compton.win_set \
#             uint32:${id} string:shadow_force uint32:${1} &>/dev/null&
#     done
# }
# cmd=(bspc config window_gap)
# gap=$(( $(${cmd[@]}) ? 0 : 12 ))
# ${cmd[@]} $gap && setshadow $(( gap ? 2 : 0 ))