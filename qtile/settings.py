# Main modifier key, 'mod4' = Super
mod = "mod4"

# Applications
terminal = "alacritty"
browser = "firefox"
file_explorer = "nautilus"
wifi_settings = 'gnome-control-center wifi'

# Menu with these entries is shown after clicking 'Menu' on the bar
system_apps = {
    '󰟀 Boxes': 'gnome-boxes',
    ' Browser': browser,
    '󰃬 Calculator': 'gnome-calculator',
    '󰃭 Calendar': 'gnome-calendar',
    ' Characters': 'gnome-characters',
    '󰥔 Clocks': 'gnome-clocks',
    ' Control Center': 'gnome-control-center',
    '󰋊 Disks': 'gnome-disks',
    '󰉋 File Explorer': file_explorer,
    ' Fonts': 'gnome-font-viewer',
    '󰘥 Help': 'gnome-help',
    ' Logs': 'gnome-logs',
    '󰍍 Maps': 'gnome-maps',
    '󰆌 Software': 'gnome-software',
    '󰋽 System Monitor': 'gnome-system-monitor',
    ' Terminal': terminal,
    '󱩽 Text Editor': 'gnome-text-editor',
    '󰖐 Weather': 'gnome-weather',
}

# Menu with these entries is shown after clicking 'Shutdown' on the bar
shutdown_menu = {
    'Power Off': 'systemctl poweroff',
    'Suspend': 'systemctl suspend',
    'Reboot': 'systemctl reboot',
    'Log Out': 'qtile cmd-obj -o cmd -f shutdown',
}

# Appearance
margin = 12
FONT = 'CaskaydiaCoveNerdFontMono'
FONT_BOLD = 'CaskaydiaCoveNerdFontMono Bold'
