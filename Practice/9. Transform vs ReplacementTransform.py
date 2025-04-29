from manim import * 

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))  # Transform a into b
        self.play(Transform(a, c))  # Transform a into c
        self.play(FadeOut(b))       # here obj A, B is alive
        self.play(FadeOut(c))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b)) # Replace a with b
        self.play(ReplacementTransform(b, c)) # Replace b with c   
        self.play(FadeOut(c))        # here obj A, B is dead

    def construct(self):
        self.transform()
        self.wait(5)  # wait for 5 seconds
        self.replacement_transform()