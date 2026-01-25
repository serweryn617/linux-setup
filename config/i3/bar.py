#!/usr/bin/env python3

import sys
sys.stderr = open("/tmp/i3_err_log", 'a')

import json
import subprocess
import time
import sys
import psutil
from pathlib import Path
import select

def run_terminal(command = None):
    term = ["alacritty", "-e", command] if command else ["alacritty"]
    subprocess.Popen(term)

def run_script(path):
    subprocess.Popen(path)

def has_line() -> bool:
    r, _, _ = select.select([sys.stdin], [], [], 0)
    return bool(r)

def read_event():
    while has_line():
        line = sys.stdin.readline().strip()

        # TODO: Workaround for initial click event missing
        if not line.startswith(','):
            continue

        line = line.lstrip(",[")
        try:
            return json.loads(line)
        except json.JSONDecodeError as e:
            pass


print('{ "version": 1, "click_events": true }')
print('[')
print('[]')
sys.stdout.flush()

cpu_loads = [0 for _ in range(10)]

while True:
    cpu_loads.pop(0)
    cpu_loads.append(psutil.cpu_percent())
    cpu = sum(cpu_loads) / 10
    battery = psutil.sensors_battery()

    blocks = [
        {"name": "menu", "full_text": " Menu "},
        # {"name": "res_1080p", "full_text": " 1080p "},
        # {"name": "res_2k", "full_text": "  2K  "},
        # {"name": "res_4k", "full_text": "  4K  "},
        {
            "name": "cpu",
            "full_text": f" CPU: {cpu:3.0f}% ",
            # "color": "#a1cfff" if cpu < 2 else "#ff5555"
        },
        {
            "name": "battery",
            "full_text": f" 🔋{battery.percent:3.0f}% "  # 🔋🪫⚡
        },
        {
            "name": "time",
            "full_text": time.strftime(" %H:%M:%S %d.%m.%Y ")
        },
        {"name": "power", "full_text": " Power "},
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
            run_script(["python3", Path("~/.config/i3/main_menu.py").expanduser().resolve()])
        if name == "power":
            run_script(["python3", Path("~/.config/i3/power_menu.py").expanduser().resolve()])

    time.sleep(0.1)