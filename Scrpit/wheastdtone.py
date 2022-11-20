import schemdraw
import schemdraw.elements as elm
schemdraw.config(lw=1, font='serif')
with schemdraw.Drawing(file='img\wheastone.pdf',show=False) as d:
    elm.style(elm.STYLE_IEC)
    d += elm.SourceV().up().length(4).label("$U_0$")
    d += elm.Line().right()
    d.push()
    d += elm.Line().right().length(4)
    d += (R3:= elm.Resistor().down().label("$R_3$")).length(2)
    d += (R4:= elm.Resistor().down().label("$R_4$")).length(2)
    d += elm.Line().left().length(4)
    d += elm.Line().left()
    d.pop()
    d += (R1:= elm.Resistor().down().label("$R_1$")).length(2)
    d += (R2:= elm.Resistor().down().label("$R_2$")).length(2)
    d += elm.Line().right().dot(open=True).at(R2.start).length(1)
    d += elm.Gap().label(('A','$\Rightarrow $','B')).length(2)
    d += elm.Line().idot(open=True).length(1)