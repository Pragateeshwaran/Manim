from manim import *

class RotateObj(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_fill(BLUE, opacity=0.5)
        triangle.rotate(45 * DEGREES)  # Rotate the triangle by 45 degrees, rotate in begining itself
        self.play(Create(triangle)) 
        self.wait(3)