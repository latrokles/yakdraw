from dataclasses import dataclass
from random import randint

from yakdraw.color import Color, Palette
from yakdraw.sketch import Sketch
from yakdraw.window import Mouse

@dataclass
class ColorPixels(Sketch):

      def handle_mouse(self, mouse: Mouse):
          if mouse.left:
             self.canvas.put_pixel(mouse.x, mouse.y, Palette.BLUE)
             return

      def setup(self):
          for y in range(self.height):
              for x in range(self.width):
                  self.canvas.put_pixel(x, y, Palette.WHITE)

      def draw(self):
          r = randint(0, 255)
          g = randint(0, 255)
          b = randint(0, 255)

          x = randint(0, self.width)
          y = randint(0, self.height)

          self.canvas.put_pixel(x, y, Color(r, g, b))
          

def main():
    ColorPixels(600, 400, 1, title='ColorPixels')