import cairocffi
import math

from libqtile import bar
from libqtile.command.base import expose_command
from libqtile.widget import base


class Powerline(base._Widget):
    defaults = [
        ("type", "mid", "Symbol type, one of open, mid, close"),
    ]

    def __init__(self, length=bar.CALCULATED, **config):
        base._Widget.__init__(self, length, **config)
        self.add_defaults(Powerline.defaults)

    def _configure(self, qtile, bar):
        base._Widget._configure(self, qtile, bar)

    def _get_bar_size(self):
        if self.bar.horizontal:
            return self.bar.height
        else:
            return self.bar.width

    def calculate_length(self):
        return self._get_bar_size() // 2

    def draw(self):
        idx = self.bar.widgets.index(self)
        max_idx = len(self.bar.widgets)

        if idx > 0 and self.bar.widgets[idx - 1].background:
            self.color_left = self.bar.widgets[idx - 1].background
        else:
            self.color_left = self.bar.background

        if idx < max_idx - 1 and self.bar.widgets[idx + 1].background:
            self.color_right = self.bar.widgets[idx + 1].background
        else:
            self.color_right = self.bar.background

        self.drawer.ctx.set_operator(cairocffi.OPERATOR_SOURCE)
        self.drawer.clear(self.color_right)

        if self.type == "mid":
            self.draw_middle()
        elif self.type == "open":
            self.draw_opening_half_circle()
        elif self.type == "close":
            self.draw_closing_half_circle()

        # if self.bar.horizontal:
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)
        # else:
        #     self.drawer.draw(offsety=self.offset, offsetx=self.offsetx, height=self.width)

    @expose_command()
    def update(self):
        self.draw()

    def draw_middle(self):
        size = self._get_bar_size()

        self.drawer.ctx.new_sub_path()
        
        self.drawer.ctx.move_to(0, 0)
        self.drawer.ctx.line_to(size // 2, 0)
        self.drawer.ctx.line_to(0, size)

        self.drawer.set_source_rgb(self.color_left)
        self.drawer.ctx.fill()

    def draw_opening_half_circle(self):
        size = self._get_bar_size()
        radius = size // 2

        self.drawer.ctx.new_sub_path()
        self.drawer.ctx.arc(
            radius,
            radius,
            radius,
            math.radians(90),
            math.radians(-90)
        )
        self.drawer.ctx.line_to(0, 0)
        self.drawer.ctx.line_to(0, size)
        self.drawer.set_source_rgb(self.color_left)
        self.drawer.ctx.fill()

    def draw_closing_half_circle(self):
        size = self._get_bar_size()
        radius = size // 2

        self.drawer.ctx.new_sub_path()
        self.drawer.ctx.arc(
            0,
            radius,
            radius,
            math.radians(-90),
            math.radians(90)
        )
        self.drawer.set_source_rgb(self.color_left)
        self.drawer.ctx.fill()

