import pandas as pd
import statsmodels.api as sm
import numpy as np

import requests, zipfile, StringIO
import pandas as pd

r = requests.get('https://resources.lendingclub.com/LoanStats3c.csv.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
loansData = pd.read_csv(z.open('LoanStats3c.csv'), nrows = 1000, skiprows=1)

#Remove the '%' symbols from the Interest.Rate column.
#loansData.int_rate = map(lambda x: x.rstrip('%'), loansData.int_rate)

subdata = pd.DataFrame(columns=['Interest.Rate', 'Annual.Income', 'Home'])
subdata['Interest.Rate'] = loansData.int_rate
subdata['Annual.Income'] = loansData.annual_inc.astype(float)
subdata['Home'] = loansData.home_ownership

#Statsmodels needs an intercept column in your dataframe, so add a column with a constant intercept of 1.0.
subdata['Intercept'] = float(1.0)

subdata.dropna(inplace=True)
subdata['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), subdata['Interest.Rate'])

#Model with monthly income
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "                         Model with monthly income                                 "
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

model1 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income']])
res1 = model1.fit()

print res1.summary()

subdata['Home'] = map(lambda x: 1*(x == "RENT") + 2*(x == "OWN"), subdata['Home'])

#Model with monthly income and home ownership
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "                 Model with monthly income and Home Ownership                      "
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
model2 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income', 'Home']])
res2 = model2.fit()
print res2.summary()

subdata['Interaction'] = subdata['Annual.Income']*subdata['Home']

#Model with monthly income and home ownership and interaction
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "          Model with monthly income, Home Ownership, and Interaction               "
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
model3 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income', 'Home', 'Interaction']])
res3 = model3.fit()
print res3.summary()

#This is really a bad model, as one can say by looking at a scatter plot and the R^2 of the fit. 


