from manim import *

class TextIn4K(Scene):
    def construct(self):
        text1 = Text("Pragateesh!", font_size=96, color=BLUE)
        text2 = Text("weds", font_size=96, color=RED)
        text3 = Text("Kayal!", font_size=96, color=BLUE)
        self.play(Write(text1))
        self.wait(1)
        self.play(Transform(text1, text2))
        self.wait(1)
        self.play(Transform(text2, text3))
        self.wait(2)
