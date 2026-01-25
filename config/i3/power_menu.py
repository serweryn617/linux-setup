#!/usr/bin/env python3

import dmenu

def run_power_menu():
    options = {
        "Power Off": ["systemctl", "poweroff"],
        "Suspend": ["systemctl", "suspend"],
        "Reboot": ["systemctl", "reboot"],
        "Log Out": ["i3-msg", "exit"],
    }
    dmenu.dmenu(options)

if __name__ == "__main__":
    run_power_menu()