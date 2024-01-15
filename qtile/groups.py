from libqtile.config import Group, Match

from settings import browser

GROUPS = [
    Group('DEV'),
    Group('NET', matches = [Match(wm_class=[browser])]),
    Group('DOC'),
]

HIDDEN_GROUPS = [
    Group('4'),
    Group('5'),
    Group('6'),
    Group('7'),
    Group('8'),
    Group('9'),
]