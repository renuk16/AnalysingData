'''
Write a script called "chi_squared.py" that loads the data, cleans it, performs the chi-squared test, and prints the result. 
'''

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove NAs
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

k = 0
for i in freq:
	k = k+1

print "The number of unique elements in freq is", k

print "The most frequent number of open credit lines is", freq.most_common(1)[0][0]

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

#Chi-squared test:
chi, p = stats.chisquare(freq.values())

print "We find a chi-squared and a p-value of", chi, p
print " The hypothesis that the all open credit lines ar uniformly distributed is disfavored." 
