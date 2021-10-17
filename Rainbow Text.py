from manim import *

class rainbow (Scene):
    def construct(self):
        r = Tex("T","E","X","T")
        r[0].set_color(RED)
        r[1].set_color(GREEN)
        r[2].set_color(BLUE)
        r[3].set_color(PURPLE)

        self.play(Write(r),run_time=5)