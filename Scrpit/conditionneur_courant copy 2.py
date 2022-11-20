import schemdraw
import schemdraw.elements as elm
elm.style(elm.STYLE_IEEE)
schemdraw.config(lw=1, font='serif')
with schemdraw.Drawing(file='img\condi_cur.pdf') as d:
    elm.style(elm.STYLE_IEC)
    d += (L1 := elm.Line()) 
    d += elm.CurrentLabelInline(direction='in').at(L1).label('$I_0$')
    d += elm.ResistorVar().down().label("$ R_x $").label(('+','$U = R \cdot I_0 $','-'), loc='bottom')
    d += elm.Line().left()
    d += elm.SourceI().up()
