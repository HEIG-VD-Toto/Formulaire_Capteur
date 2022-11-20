import schemdraw
import schemdraw.elements as elm
schemdraw.config(lw=1, font='serif')
with schemdraw.Drawing(file='img\circuit_res.pdf') as d:
    elm.style(elm.STYLE_IEC)
    d += elm.SourceV().length(4).label("$U_0$")
    d += elm.Resistor().right().label("$R_o$").length(4)
    d += elm.Dot()
    d.push()
    d += (Lb := elm.Inductor2().down().label("$L_b(X)$")).length(2)
    d += (Rb := elm.Resistor().down().label("$R_b(X)$")).length(2)
    d += elm.Dot()
    d.pop()
    d += elm.Line().right()
    d += (C := elm.Capacitor().down().label("C").length(4))
    d += elm.Line().left()
    d += elm.Line().length(4).left()
    d += (bobine := elm.EncircleBox([Lb, Rb], padx=.10).linestyle('--').linewidth(1).color('red').label("Bobine de mesure",loc = "right", rotate=-90))
    d += (inpedance := elm.EncircleBox([bobine, C], padx=.10).linestyle('--').linewidth(1).color('blue').label(r"$Z_{eq}$",loc = "right", rotate=-90))