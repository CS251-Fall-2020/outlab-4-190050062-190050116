import requests
import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

url = 'https://api.covid19india.org/csv/latest/case_time_series.csv'
r = requests.get(url)
with open('case_time_series.csv', 'wb') as f:
   f.write(r.content)
df=pd.read_csv('case_time_series.csv')
i=(df.index[df['Date'] == '15 April '].tolist())[0]
l=len(df.index)
h=[]
while i<l:
	h=h+[df['Total Deceased'].values[i]/df['Total Deceased'].values[i-1]]
	i=i+1
ht=np.array(h)
t=np.arange(1, ht.shape[0]+1)
slope, intercept, r_value, p_value, std_err = stats.linregress(t, ht)

plt.plot(t, ht, 'o', label='Actual data points')
plt.plot(t, intercept + slope*t, 'r', label='Fitted line')
plt.xlabel('t')
plt.ylabel('H(t)')
plt.title('Levitt Metric for COVID19 India')
plt.legend()
plt.savefig('covid.png')

print(int(round((1-intercept)/slope)))