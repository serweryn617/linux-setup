import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


@hook.subscribe.client_new
def display_password_terminal(client):
    if client.name == 'password-terminal':
        client.set_size_floating(800, 300)


@hook.subscribe.client_new
def display_info_terminal(client):
    if client.name == 'info-terminal':
        client.set_size_floating(800, 800)
