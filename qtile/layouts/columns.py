from libqtile.layout.columns import Columns


from libqtile.config import ScreenRect
from libqtile.backend.base import Window


class MyColumns(Columns):
    def __init__(self, **config):
        super().__init__(**config)
        self.border_focus_original = self.border_focus

    def configure(self, client: Window, screen_rect: ScreenRect) -> None:
        is_single = len(self.columns) == 1 and len(self.columns[0]) == 1
        self.border_focus = self.border_normal if is_single else self.border_focus_original
        super().configure(client, screen_rect)
