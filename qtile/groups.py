from libqtile.config import Group, Match

from settings import browser

GROUPS = [
    Group('DEV'),
    Group('NET', matches = [Match(wm_class=[browser])]),
    Group('DOC'),
]