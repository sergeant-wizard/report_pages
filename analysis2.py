import matplotlib.pyplot
import numpy

import my_module.hoge


x = numpy.linspace(-6, 6, 12)
matplotlib.pyplot.plot(
    x, numpy.sin(x))
matplotlib.pyplot.savefig('docs/assets/analysis2/chart.png')
