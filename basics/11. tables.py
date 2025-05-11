from manim import *

class TableExample(Scene):
    def construct(self):
        # Table data
        data = [
            ["Name", "Age", "City"],
            ["Alice", "24", "New York"],
            ["Bob", "30", "London"],
            ["Charlie", "22", "Berlin"]
        ]

        # Create a table
        table = Table(
            data,
            include_outer_lines=True  # Draws border lines
        )

        circle = Circle()
        self.play(ReplacementTransform(circle, table))
        # self.play(Create(table))
        self.wait(2)
