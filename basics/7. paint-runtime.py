from manim import *

class paint(Scene):
    def construct(self):
        self.triangle = Triangle()
        self.circle = Circle()
        self.circle.set_stroke(RED_E, width=10, opacity=3).set_fill(BLUE_B, opacity=3)
        print(self.triangle, self.circle, Triangle())
        self.triangle.set_stroke(RED_E, width=10, opacity=3).set_fill(BLUE_B, opacity=3)
        self.play(Create(self.triangle))
        self.wait(2)
        # self.play(
        #     self.triangle.animate.set_fill(WHITE, opacity=10), 
        #     Transform(self.triangle, self.circle), 
        #     run_time=2
        # )

        self.play(self.triangle.animate.set_fill(WHITE, opacity=1), run_time=1)
        self.wait(1)  # Another break after color change (1 second pause)

        # Animation 3: Transform the triangle into a circle
        self.play(Transform(self.triangle, self.circle), run_time=2)
        self.wait(2)  # Final wait after transformation

        self.wait(2)