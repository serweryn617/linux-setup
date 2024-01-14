from libqtile.lazy import lazy
from libqtile.extension import CommandSet, DmenuRun

import colors
from apps import system_apps
from settings import *

def get_dmenu_settings(command):
    sel = colors.darker_gray 
    custom_command = (
        command + ' -c -bw 2' +
        ' -nhf ' + colors.pink2 +
        ' -shf ' + colors.pink1 +
        ' -nhb ' + colors.bg_dark +
        ' -shb ' + sel +
        ' -bc ' + colors.green1
    )
    theme = {
        'dmenu_command': custom_command,
        'dmenu_font': FONT,
        'background': colors.bg_dark,
        'foreground': colors.text,
        'selected_background': sel,
        'selected_foreground': colors.white,
        'dmenu_height': 24,
        'dmenu_lines': 10,
        'dmenu_ignorecase': True,
    }
    return theme

def dmenu_run():
    return lazy.run_extension(DmenuRun(
        **get_dmenu_settings('dmenu_run'),
        dmenu_prompt = '󰍉'
    ))

def dmenu_sys():
    return lazy.run_extension(CommandSet(
        **get_dmenu_settings('dmenu'),
        commands = system_apps,
    ))
