from manim import *
import numpy as np

class FourierSeriesScene(Scene):
    def construct(self):
        heading = Text("Fourier Series Decomposition", font_size=40)
        heading.to_edge(UP)

        self.play(Write(heading))
        self.wait(0.5)

        graph_axes = Axes(
            x_range=[0, 4 * np.pi, np.pi],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE_D},
            tips=False
        ).shift(DOWN * 0.5)

        self.play(
            Create(graph_axes),
            Write(graph_axes.get_x_axis_label("t")),
            Write(graph_axes.get_y_axis_label("f(t)"))
        )
        self.wait(0.5)

        target_curve = graph_axes.plot(
            lambda x: 4 / np.pi * np.sign(np.sin(x)),
            color=WHITE,
            stroke_width=2,
            use_vectorized=False
        )

        target_text = Text(
            "Target Square Wave",
            font_size=16,
            color=WHITE
        ).next_to(target_curve, UR, buff=-0.5)

        harmonic_values = [1, 3, 5, 7, 9]
        palette = [RED, BLUE, GREEN, YELLOW, PURPLE]

        displayed_curves = []
        displayed_labels = []
        accumulated_terms = []

        for position, harmonic in enumerate(harmonic_values):
            current_color = palette[position]

            term = lambda x, k=harmonic: (4 / (np.pi * k)) * np.sin(k * x)
            accumulated_terms.append(term)

            curve = graph_axes.plot(
                term,
                color=current_color,
                stroke_width=2,
                stroke_opacity=0.6
            )

            displayed_curves.append(curve)

            harmonic_label = MathTex(
                f"n = {harmonic}",
                color=current_color,
                font_size=24
            ).to_edge(RIGHT, buff=0.5).shift(
                UP * (1.5 - 0.4 * position)
            )

            displayed_labels.append(harmonic_label)

            self.play(Create(curve), Write(harmonic_label), run_time=1)
            self.wait(0.5)

            def partial_sum(x, pieces=list(accumulated_terms)):
                return sum(piece(x) for piece in pieces)

            approximation = graph_axes.plot(
                partial_sum,
                color=ORANGE,
                stroke_width=4
            )

            if position == 0:
                self.play(
                    Transform(curve.copy(), approximation),
                    run_time=1.5
                )
                active_curve = approximation
            else:
                self.play(
                    Transform(active_curve, approximation),
                    run_time=1.5
                )

            self.wait(1)

        self.play(FadeIn(target_curve), Write(target_text))
        self.wait(2)

        everything = VGroup(*displayed_curves, *displayed_labels)
        self.play(FadeOut(everything), run_time=1.5)

        self.wait(2)