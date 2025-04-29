from manim import *

class CreateObj(Scene):
    def construct(self):
        triangle = Triangle() 
        triangle.set_fill(BLUE, opacity=0.5) # set the color and opacity of the triangle
        self.play(Create(triangle))
        self.wait(5)