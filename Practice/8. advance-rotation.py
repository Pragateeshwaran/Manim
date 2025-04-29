from manim import *

class rotate(Scene):
    def construct(self):
        triangle = Triangle(color=BLUE, fill_opacity=0.7).shift(2*LEFT)  # Create a triangle and shift it to the left from origin
        triangle.set_stroke(WHITE, width=10)
        square = Square(color=RED, fill_opacity=0.7).shift(2*RIGHT)  # Create a circle and shift it to the right from origin
        square.set_stroke(WHITE, width=10)
        # self.play(
        #     triangle.animate.rotate(PI), 
        #     Rotate(square, angle=PI),  # Rotate the circle by 180 degrees    ====> for simultaneous animation 
        #     runtime = 10
        # )

        self.play(triangle.animate.rotate(PI), run_time=5)
        self.play(Rotate(square, angle=PI), run_time=5)

        self.wait(10)