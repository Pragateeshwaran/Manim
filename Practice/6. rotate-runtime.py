from manim import *

class RotateObj(Scene):
    def construct(self):
        triangle = Triangle()
        triangle.set_stroke(WHITE, width=10)
        triangle.set_fill(RED, opacity=0.5)
        self.play(Create(triangle))  # Create the triangle first
        self.wait(1)
        self.play(triangle.animate.rotate(180 * DEGREES))  # Rotate the triangle by 45 degrees
        self.wait(3)