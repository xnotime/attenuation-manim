import manim as m

class Eqn(m.Scene):
    def construct(self):
        eqn = m.Tex(r'$E \neq mc^2$', font_size= 60)
        self.play(m.Write(eqn))
