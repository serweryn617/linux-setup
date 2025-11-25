#!/usr/bin/env python3

import json
import subprocess
import time
import sys
import psutil
from pathlib import Path

def run_terminal(command = None):
    term = ["i3-sensible-terminal", "-e", command] if command else ["i3-sensible-terminal"]
    subprocess.Popen(term)

def run_script(path):
    subprocess.Popen(path)

def read_event():
    line = sys.stdin.readline().strip()
    while line.startswith(",") or line.startswith("["):
        line = line[1:].strip()
    if not line:
        return
    try:
        return json.loads(line)
    except json.JSONDecodeError as e:
        pass


print('{ "version": 1, "click_events": true }')
print('[')
print('[]')
sys.stdout.flush()

while True:
    cpu = psutil.getloadavg()[0]
    battery = psutil.sensors_battery()

    blocks = [
        {"name": "menu", "full_text": "  Menu  "},
        {"name": "res_1080p", "full_text": " 1080p "},
        {"name": "res_2k", "full_text": "  2K  "},
        {"name": "res_4k", "full_text": "  4K  "},
        {
            "name": "cpu",
            "full_text": f"CPU: {cpu:.2f}",
            # "color": "#a1cfff" if cpu < 2 else "#ff5555"
        },
        {
            "name": "battery",
            "full_text": f"🔋{battery.percent:.0f}%"  # 🔋🪫⚡
        },
        {
            "name": "time",
            "full_text": time.strftime("%H:%M:%S %Y-%m-%d")
        }
    ]

    print("," + json.dumps(blocks))
    sys.stdout.flush()

    event = read_event()
    
    if event:
        name = event.get("name")

        if name == "cpu":
            run_terminal("top")
        if name == "time":
            run_terminal()
        if name == "menu":
            run_script(Path("~/.config/scripts/main_menu.sh").expanduser().resolve())

        if name == "res_1080p":
            run_script(Path("~/.config/scripts/res_1080p.sh").expanduser().resolve())
        if name == "res_2k":
            run_script(Path("~/.config/scripts/res_2k.sh").expanduser().resolve())
        if name == "res_4k":
            run_script(Path("~/.config/scripts/res_4k.sh").expanduser().resolve())

    time.sleep(0.1)