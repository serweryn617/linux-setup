#!/usr/bin/env python3

import json
import subprocess
import time
import sys
import psutil
import select
import queue
from pathlib import Path

event_queue = queue.Queue()

def run_terminal(command = None):
    term = ["i3-sensible-terminal", "-e", command] if command else ["i3-sensible-terminal"]
    subprocess.Popen(term)

def run_script(path):
    subprocess.Popen(path)

def log(msg):
    with open("/home/seweryn/i3_bar_log", "a") as f:
        f.write(msg)
        f.write("\n")

def read_event():
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline().strip()
        log(f"EVENT: {line}")
        while line.startswith(",") or line.startswith("["):
            line = line[1:].strip()
        if not line:
            # continue
            log("DISCARDING")
            return
        try:
            event = json.loads(line)
            event_queue.put(event)
        except Exception as e:
            log("EXCEPTION")
            log("STR", str(e))
            log(type(e).__name__)
            log("EVENT:", event)
            log("LEN", len(event))


print('{ "version": 1, "click_events": true }')
print('[')
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

    print(json.dumps(blocks) + ",")
    sys.stdout.flush()

    read_event()
    
    while not event_queue.empty():
        log(f"PROCESSING")
        event = event_queue.get()
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