
from manim import *
import numpy as np

class FourierSeriesScene(Scene):
    def construct(self):
        title = Text("Fourier Series Decomposition", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 4 * np.pi, np.pi],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE_D},
            tips=False
        ).shift(DOWN * 0.5)

        x_label = axes.get_x_axis_label("t")
        y_label = axes.get_y_axis_label("f(t)")
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        square_wave = axes.plot(
            lambda t: 4 / np.pi * np.sign(np.sin(t)),
            color=WHITE,
            stroke_width=2,
            use_vectorized=False
        )
        square_wave_label = Text("Target Square Wave", font_size=16, color=WHITE).next_to(square_wave, UR, buff=-0.5)

        harmonics_n = [1, 3, 5, 7, 9]
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE]
        
        harmonic_plots = []
        labels = []
        cumulative_functions = []

        for idx, n in enumerate(harmonics_n):
            color = colors[idx]
            
            harmonic_func = lambda t, n_val=n: (4 / (np.pi * n_val)) * np.sin(n_val * t)
            cumulative_functions.append(harmonic_func)

            harmonic_plot = axes.plot(
                harmonic_func,
                color=color,
                stroke_width=2,
                stroke_opacity=0.6
            )
            harmonic_plots.append(harmonic_plot)

            label = MathTex(
                f"n = {n}", 
                color=color, 
                font_size=24
            ).to_edge(RIGHT, buff=0.5).shift(UP * (1.5 - idx * 0.4))
            labels.append(label)

            self.play(Create(harmonic_plot), Write(label), run_time=1)
            self.wait(0.5)

            def current_approximation(t, funcs=list(cumulative_functions)):
                return sum(f(t) for f in funcs)

            approximation_plot = axes.plot(
                current_approximation,
                color=ORANGE,
                stroke_width=4
            )

            if idx == 0:
                self.play(Transform(harmonic_plot.copy(), approximation_plot), run_time=1.5)
                active_approximation = approximation_plot
            else:
                self.play(Transform(active_approximation, approximation_plot), run_time=1.5)
            
            self.wait(1)

        self.play(FadeIn(square_wave), Write(square_wave_label))
        self.wait(2)

        all_harmonics = VGroup(*harmonic_plots, *labels)
        self.play(FadeOut(all_harmonics), run_time=1.5)
        self.wait(2)
