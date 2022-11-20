import schemdraw
import schemdraw.elements as elm
from schemdraw import flow
elm.style(elm.STYLE_IEEE)
schemdraw.config(lw=1, font='serif')
with schemdraw.Drawing(file='img\condi_ten.pdf') as d:
    elm.style(elm.STYLE_IEC)
    d += (R1:= elm.Resistor().right().label("$R_0$"))
    d += (R2:= elm.ResistorVar().down().label("$R_x$").label(r"$U(R) = \frac{R}{R+R_0} \cdot U_0 )$",loc="bottom"))
    d += elm.Line().left()
    d += elm.SourceV().up().label("$U_0$")
