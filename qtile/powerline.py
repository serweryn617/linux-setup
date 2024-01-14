import math

from libqtile import bar
from libqtile.command.base import expose_command
from libqtile.widget import base


# from libqtile.log_utils import logger


class Powerline(base._Widget):
    defaults = [
        ("type", "mid", "Symbol type, one of open, mid, close"),
        ("radius_delta", 0, "Add this delta to the arc radius"),
        ("y_offset", 0, "Adjust Y position"),
        # ("auto_color", True, "Use background colors from neighboring widgets in the middle and bar background color in opening and closing symbols"),
        ("color_left", None, "Powerline symbol left side color"),
        ("color_right", None, "Powerline symbol right side color"),
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
        
        if self.type == "mid":
            self.drawer.clear(self.color_right or self.bar.background)
            self.draw_middle()
        elif self.type == "open":
            self.drawer.clear(self.color_left or self.bar.background)
            self.draw_opening_half_circle()
        elif self.type == "close":
            self.drawer.clear(self.color_right or self.bar.background)
            self.draw_closing_half_circle()

        # if self.bar.horizontal:
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)
        # else:
        #     self.drawer.draw(offsety=self.offset, offsetx=self.offsetx, height=self.width)

    def draw_middle(self):
        size = self._get_bar_size()

        self.drawer.ctx.new_sub_path()
        
        self.drawer.ctx.move_to(0, 0)
        self.drawer.ctx.line_to(size // 2, 0)
        self.drawer.ctx.line_to(0, size)

        self.drawer.set_source_rgb(self.color_left)
        self.drawer.ctx.fill()

    def draw_opening_half_circle(self):
        radius = self.calculate_length()

        self.drawer.ctx.new_sub_path()
        self.drawer.ctx.arc(
            radius,
            radius + self.y_offset,
            radius + self.radius_delta,
            math.radians(90),
            math.radians(-90)
        )
        self.drawer.set_source_rgb(self.color_right)
        self.drawer.ctx.fill()

    def draw_closing_half_circle(self):
        radius = self.calculate_length()

        self.drawer.ctx.new_sub_path()
        self.drawer.ctx.arc(
            0,
            radius + self.y_offset,
            radius + self.radius_delta,
            math.radians(-90),
            math.radians(90)
        )
        self.drawer.set_source_rgb(self.color_left)
        self.drawer.ctx.fill()

    @expose_command()
    def update(self):
        self.draw()
