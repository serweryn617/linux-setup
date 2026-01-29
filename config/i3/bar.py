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

def cpu_indicator():
    cpu_loads.pop(0)
    cpu_loads.append(psutil.cpu_percent())
    cpu = sum(cpu_loads) / 10
    return f" 🧮 CPU: {cpu:3.0f}% "

def time_left(seconds):
    mm, ss = divmod(seconds, 60)
    hh, mm = divmod(mm, 60)
    return f"{hh:2d}:{mm:02d}"

def battery_indicator():
    battery = psutil.sensors_battery()
    symbol = "🔋" if battery.percent >= 30 else "🪫"
    symbol = "⚡" if battery.power_plugged else symbol
    left = time_left(battery.secsleft)
    # 🔋🪫⚡
    return f" {symbol}{battery.percent:3.0f}% (⏳{left}) "

def memory_indicator():
    memory = psutil.virtual_memory()

    def gb(x):
        return (x // (1000**3 // 10)) / 10

    total = gb(memory.total)
    used = gb(memory.total - memory.available)

    total = f"{total:.1f}"
    used = f"{used:.1f}"

    space = len(total)
    pad = space - len(used)

    return f" 💾 MEM: {memory.percent:3.0f}% {' ' * pad}({used}/{total}GB) "

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
    blocks = [
        {"name": "menu", "full_text": " 📑 Menu "},
        {
            "name": "cpu",
            "full_text": cpu_indicator(),
        },
        {
            "name": "mem",
            "full_text": memory_indicator(),
        },
        {
            "name": "battery",
            "full_text": battery_indicator(),
        },
        {
            "name": "time",
            "full_text": time.strftime(" 🕒 %H:%M:%S 📅 %d.%m.%Y ")
        },
        {"name": "power", "full_text": " 💥 Power "},
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