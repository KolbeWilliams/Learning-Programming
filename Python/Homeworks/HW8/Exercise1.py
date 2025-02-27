#Exercise 1:
import pandas as pd
from functools import reduce

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82], 'Thu': [75, 97], 'Fri': [62, 79]}
temps_DF = pd.DataFrame(temps, index = ['Low', 'High'])
print(temps_DF)
print('\nMonday Through Wednesday:\n', temps_DF.loc[:, 'Mon':'Wed'])
print('\nLow for each day:\n', temps_DF.loc[:'Low', :])
pd.set_option('display.precision', 2)
print('\nAverage for each day:')
day_mean = reduce(lambda x, y: x + y, temps_DF.loc[:, 'Mon'])
day_mean /= len(temps_DF.loc[:, 'Mon'])
for x in range(len(temps_DF.keys())):
    li = temps_DF.keys()
    day_mean = reduce(lambda x, y: x + y, temps_DF.loc[:, li[x]])
    day_mean /= len(temps_DF.loc[:, li[x]])
    print(f'{li[x]}:', '{:.2f}'.format(day_mean))
print('\nAverage Low Temperature:', end = '')
print('{:.2f}'.format(temps_DF.loc['Low'].mean()))
print('Average High Temperature:', end = '')
print('{:.2f}'.format(temps_DF.loc['High'].mean()))
print()