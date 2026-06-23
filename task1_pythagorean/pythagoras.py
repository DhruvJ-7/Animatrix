from manim import *

class PythagorasScene(Scene):
    def construct(self):
        heading = Text("The Pythagorean Theorem", font_size=40).to_edge(UP)

        formula = MathTex(
            "a^2", "+", "b^2", "=", "c^2",
            font_size=42
        ).next_to(heading, DOWN, buff=0.3)

        formula[0].set_color(RED)
        formula[2].set_color(BLUE)
        formula[4].set_color(GREEN)

        self.play(Write(heading))
        self.play(Write(formula))
        self.wait(1)

        p1 = np.array([-2, -1.5, 0])
        p2 = np.array([2, -1.5, 0])
        p3 = np.array([-2, 1.5, 0])

        right_triangle = Polygon(
            p1, p2, p3,
            stroke_color=WHITE,
            stroke_width=3
        )

        side_a = MathTex("a").next_to(
            Line(p3, p1).get_center(),
            LEFT,
            buff=0.2
        )

        side_b = MathTex("b").next_to(
            Line(p1, p2).get_center(),
            DOWN,
            buff=0.2
        )

        side_c = MathTex("c").next_to(
            Line(p2, p3).get_center(),
            UR,
            buff=0.1
        )

        self.play(Create(right_triangle))
        self.play(
            Write(side_a),
            Write(side_b),
            Write(side_c)
        )

        self.wait(1.5)

        red_square = Polygon(
            p1,
            p3,
            p3 + LEFT * 3,
            p1 + LEFT * 3,
            fill_color=RED,
            fill_opacity=0.5,
            stroke_color=RED
        )

        red_text = MathTex(
            "a^2",
            color=RED
        ).move_to(red_square.get_center())

        blue_square = Polygon(
            p1,
            p2,
            p2 + DOWN * 4,
            p1 + DOWN * 4,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_color=BLUE
        )

        blue_text = MathTex(
            "b^2",
            color=BLUE
        ).move_to(blue_square.get_center())

        hypotenuse_vector = p2 - p3
        normal_vector = np.array(
            [-hypotenuse_vector[1], hypotenuse_vector[0], 0]
        )

        green_square = Polygon(
            p3,
            p2,
            p2 + normal_vector,
            p3 + normal_vector,
            fill_color=GREEN,
            fill_opacity=0.5,
            stroke_color=GREEN
        )

        green_text = MathTex(
            "c^2",
            color=GREEN
        ).move_to(green_square.get_center())

        self.play(
            FadeIn(red_square, target_position=right_triangle),
            Write(red_text)
        )

        self.wait(1)

        self.play(
            FadeIn(blue_square, target_position=right_triangle),
            Write(blue_text)
        )

        self.wait(1)

        self.play(
            FadeIn(green_square, target_position=right_triangle),
            Write(green_text)
        )

        self.wait(2)

        self.play(
            Indicate(formula, scale_factor=1.2),
            Flash(green_text, color=GREEN, flash_radius=0.7)
        )

        self.wait(3)