'''
Write a script called "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson. Make sure your plots have names that are reasonably descriptive. Push your code to GitHub and enter the link below.
'''

import collections
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import scipy.stats as stats

#Data in this lesson
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#boxPlot
p1 = plt.figure(1)
plt.boxplot(x)
plt.title('BoxPlot')
p1.savefig('prob-boxplot.pdf', format='pdf')

#Hist
p2 = plt.figure(2)
plt.hist(x)
plt.title('Historgram')
p2.savefig('prob-hist.pdf', format='pdf')

#QQ Plot
p3 = plt.figure(3)
stats.probplot(x, dist="norm", plot=plt)
p3.savefig('prob-qq.pdf', format='pdf')

plt.show()


