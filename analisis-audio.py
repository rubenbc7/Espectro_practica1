import sys
sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave

import thinkplot

waveTelefono = read_wave("telefono.wav")
waveTelefono.plot()
decorate(xlabel="Tiempo (s)")
thinkplot.show()


#spectro = waveTelefono.make_spectrum()
#espectro.plot()
#decorate(xlabel="Frecuencia(Hz)")
#thinkplot.show()

wavePrimerDigito = waveTelefono.segment(start=0,duration=0.5)
#wavePrimerDigito.plot()
#decorate(xlabel="Timepo(s)")
#thinkplot.show()

#Telefono:22-4

espectroPrimerDigito = wavePrimerDigito.make_spectrum()
espectroPrimerDigito.plot()
decorate(xlabel="Frecuencia(Hz)")
thinkplot.show()

waveSegundoDigito = waveTelefono.segment(start=0.5,duration=0.5)
espectroSegundoDigito = waveSegundoDigito.make_spectrum()
espectroSegundoDigito.plot()
decorate(xlabel="Frecuencia(Hz)")
thinkplot.show()

waveTercerDigito = waveTelefono.segment(start=1.0, duration=0.5)
espectroTercerDigito = waveTercerDigito.make_spectrum()
espectroTercerDigito.plot()
decorate(xlabel="Frecuencia (Hz)")
thinkplot.show()