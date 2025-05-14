from manim import *

class PlotGraph(Scene):
    def construct(self):
        # Create Grid using NumberPlane
        grid = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            }
        )

        # Create Axes (no tips)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            x_length=6,
            y_length=6,
            tips=False,
            axis_config={"color": WHITE},
        )

        # Axis labels
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function graph
        graph = axes.plot(lambda x: x**2, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="x^2")

        # Animate
        self.play(Create(grid), Create(axes), Write(axis_labels), run_time=2)
        self.play(Create(graph), Write(graph_label), run_time=2)
        self.wait(2)
