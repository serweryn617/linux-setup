import re

from libqtile.config import Group, Match, ScratchPad, DropDown

from settings import browser, terminal

SCRATCH_PADS = [
    ScratchPad("scratchpad", [
        DropDown(
            "temp",
            terminal,
            opacity = 1,
            x = 0.25, y = 0.25, width = 0.5, height = 0.5
        ),
    ])
]

GROUPS = [
    Group('DEV'),
    Group('NET', matches = [Match(wm_class=re.compile(browser))]),
    Group('DOC'),
]

HIDDEN_GROUPS = [
    Group('4'),
    Group('5'),
    Group('6'),
    Group('7'),
    Group('8'),
    # Group('9'),
]