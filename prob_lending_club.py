import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove NAs
loansData.dropna(inplace=True)

#Boxplot of Loan amounts
loansData.boxplot(column=['Amount.Funded.By.Investors', 'Amount.Requested'])
plt.savefig('lendingclub-boxplot.pdf', format='pdf')
'''
The box plot tells us the investors funded about $10000 on average.
'''

#Hist
loansData.hist(column=['Amount.Funded.By.Investors', 'Amount.Requested'], layout=(2,1))
plt.savefig('lendingclub-hist.pdf', format='pdf')
'''
The histogram shows the distribution of funding. Whereas the box plot shows the quantile information and the 50th percentile.
'''

plt.figure()
plt.subplot(211)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.subplot(212)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('lendingclub-qq.pdf', format='pdf')

plt.show()
'''
The data does not obey a normal distribution; compared to a normal distribution, its more concentrated on the tails.
'''

'''
Comparision of the Amount Requested and Amount Funded by the Investors:
- The box plot tells us the average for both quantities are the same. However, the amount funded at the third quartile is smaller.
- The histogram tells us that the two have the same distribution, but overall there is a slight decrease in the frequencies.
- The QQ plot shows that the distributions are almost similar, showing no preference by the investors for smaller or higher amounts.
'''





