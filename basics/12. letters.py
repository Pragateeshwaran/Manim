from manim import *

class TextIn4K(Scene):
    def construct(self):
        text = Text("Pragateesh!", font_size=96, color=BLUE)
        circle = Circle(radius=1, color=RED)
        self.play(Transform(circle, text))
        self.wait(2)
