import ctypes
import sdl2
import sys

from dataclasses import dataclass

from yakdraw.color import Palette
from yakdraw.sketch import Sketch
from yakdraw.window import Mouse


WIDTH = 640
HEIGHT = 480
SCALE = 2


@dataclass
class SdlTestSketch(Sketch):
    def setup(self):
        for y in range(self.height):
            for x in range(self.width):
                self.canvas.put_pixel(x, y, Palette.WHITE)

    def handle_mouse(self, mouse: Mouse):
        if mouse.left:
            self.canvas.put_pixel(mouse.x, mouse.y, Palette.BLUE)
            return

def test():
    SdlTestSketch(WIDTH, HEIGHT, SCALE, title='sdltestsketch')