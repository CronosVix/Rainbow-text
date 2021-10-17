from manim import *

class rainbow (Scene):
    def construct(self):
        r = Tex("C","R","O","N","O","S","V","I","X")
        r[0].set_color(RED)
        r[1].set_color(ORANGE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(BLUE)
        r[5].set_color(PURPLE)
        r[6].set_color(TEAL)
        r[7].set_color(GREEN)
        r[8].set_color(ORANGE)

        self.play(Write(r),run_time=5)