import manim as m

class Eqn(m.Scene):
    def construct(self):
        with_ce = m.TexTemplate()
        with_ce.add_to_preamble(r"\usepackage[version=4]{mhchem}")
        table = m.Table(
            [["This", "is a"],
            ["simple", "Table."]],
            row_labels= [m.Tex("Shielded"), m.Tex("Unshielded")],
            col_labels= [m.Tex(r"From \ce{^241Am}", tex_template= with_ce), m.Tex("Background")],
        )
        self.play(m.Create(table))
        self.wait(5)
