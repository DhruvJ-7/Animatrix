
from manim import *

class PythagorasScene(Scene):
    def construct(self):
        title = Text("The Pythagorean Theorem", font_size=40).to_edge(UP)
        equation = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=42).next_to(title, DOWN, buff=0.3)
        equation[0].set_color(RED)
        equation[2].set_color(BLUE)
        equation[4].set_color(GREEN)
        self.play(Write(title))
        self.play(Write(equation))
        self.wait(1)
        A = np.array([-2, -1.5, 0])
        B = np.array([2, -1.5, 0])
        C = np.array([-2, 1.5, 0])
        triangle = Polygon(A, B, C, stroke_color=WHITE, stroke_width=3)
        label_a = MathTex("a").next_to(Line(C, A).get_center(), LEFT, buff=0.2)
        label_b = MathTex("b").next_to(Line(A, B).get_center(), DOWN, buff=0.2)
        label_c = MathTex("c").next_to(Line(B, C).get_center(), UR, buff=0.1)
        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1.5)
        square_a = Polygon(
            A, C, C + LEFT * 3, A + LEFT * 3,
            fill_color=RED, fill_opacity=0.5, stroke_color=RED
        )
        label_sq_a = MathTex("a^2", color=RED).move_to(square_a.get_center())
        square_b = Polygon(
            A, B, B + DOWN * 4, A + DOWN * 4,
            fill_color=BLUE, fill_opacity=0.5, stroke_color=BLUE
        )
        label_sq_b = MathTex("b^2", color=BLUE).move_to(square_b.get_center())
        v_c = B - C
        perp_v_c = np.array([-v_c[1], v_c[0], 0])
        square_c = Polygon(
            C, B, B + perp_v_c, C + perp_v_c,
            fill_color=GREEN, fill_opacity=0.5, stroke_color=GREEN
        )
        label_sq_c = MathTex("c^2", color=GREEN).move_to(square_c.get_center())
        self.play(FadeIn(square_a, target_position=triangle), Write(label_sq_a))
        self.wait(1)
        self.play(FadeIn(square_b, target_position=triangle), Write(label_sq_b))
        self.wait(1)
        self.play(FadeIn(square_c, target_position=triangle), Write(label_sq_c))
        self.wait(2)
        self.play(
            Indicate(equation, scale_factor=1.2),
            Flash(label_sq_c, color=GREEN, flash_radius=0.7)
        )
        self.wait(3)
