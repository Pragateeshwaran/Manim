from manim import *

class CreateObj(Scene):
    def construct(self):
        triangle = Triangle() 
        triangle.set_fill(BLUE, opacity=0.5)
        self.play(Create(triangle))
        self.wait(1)

        square = Square()
        square.set_fill(RED, opacity=0.5)
        self.play(Transform(triangle, square))
        self.wait(1)

        circle = Circle()
        circle.set_fill(GREEN, opacity=0.5)
        self.play(Transform(triangle, circle))  # Keep transforming the same Mobject
        self.wait(5)
