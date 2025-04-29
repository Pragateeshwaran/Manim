from manim import *
class CreateObj(Scene):
    def construct(self): # constructor is a method that is called when the object is created, like main in c, c++

        # square = Square()
        triangle = Triangle() # create object and manipulate it

        self.add(triangle, Square()) # Add the shapes to the scene

        self.wait(5) # total seconds to wait for the scene to finish   
        self.remove(triangle)
        self.add(Circle())
        self.wait(5) # total seconds to wait for the scene to finish
        self.play(Create(triangle))
        self.wait(5) # total seconds to wait for the scene to finish