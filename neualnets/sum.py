from manim import *

class ManualNeuralNetwork(Scene):
    def construct(self):
        # ─── 1. Create & position the nodes ────────────────────────────
        input_nodes  = VGroup(*[Circle(radius=0.2) for _ in range(3)])
        hidden_nodes = VGroup(*[Circle(radius=0.2) for _ in range(4)])
        output_nodes = VGroup(*[Circle(radius=0.2) for _ in range(2)])

        for i, node in enumerate(input_nodes):
            node.move_to(LEFT * 4 + UP * (i - 1) * 1.5)
        for i, node in enumerate(hidden_nodes):
            node.move_to(UP * (i - 1.5) * 1.5)
        for i, node in enumerate(output_nodes):
            node.move_to(RIGHT * 4 + UP * (i - 0.5) * 1.5)

        # ─── 2. Draw nodes ──────────────────────────────────────────────
        self.play(*[Create(n) for n in input_nodes],   run_time=1)
        self.play(*[Create(n) for n in hidden_nodes],  run_time=1)
        self.play(*[Create(n) for n in output_nodes],  run_time=1)

        # ─── 3. Connect with edges ─────────────────────────────────────
        edges = VGroup()
        for src in input_nodes:
            for tgt in hidden_nodes:
                edges.add(Line(src.get_center(), tgt.get_center()))
        for src in hidden_nodes:
            for tgt in output_nodes:
                edges.add(Line(src.get_center(), tgt.get_center()))

        self.play(*[Create(e) for e in edges], run_time=2)

        # ─── 4. Manual forward-pass highlight ───────────────────────────
        #    highlight each layer in turn
        for layer in (input_nodes, hidden_nodes, output_nodes):
            self.play(
                *[n.animate.set_fill(YELLOW, opacity=1.0) for n in layer],
                run_time=1
            )
            self.wait(0.3)

        self.wait(2)
