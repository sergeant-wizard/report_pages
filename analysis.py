import matplotlib.pyplot
import numpy
import pandas

import my_module.hoge


pandas.DataFrame(
    my_module.hoge.get_results(),
    index=['s1', 's2', 's3']
).to_html('docs/_includes/table.html')

x = numpy.linspace(-6, 6, 12)
matplotlib.pyplot.plot(
    x, numpy.sin(x))
matplotlib.pyplot.savefig('docs/images/chart.png')
