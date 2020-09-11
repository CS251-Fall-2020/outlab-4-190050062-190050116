import numpy as np

label=np.genfromtxt('mumbai_data.csv',delimiter=',', dtype= str)
label=label[0:1,1:]
value=np.genfromtxt('mumbai_data.csv',delimiter=',')
value=value[1:,1:]

std=np.around(np.std(value, axis=0, keepdims=True), decimals=3)
mean=np.around(np.mean(value, axis=0, keepdims=True), decimals=3)

out=[['Field', 'Mean', 'Std. Dev.']]
c=label.shape[1]
for i in range(c):
	out=out + [[label[0][i], str(mean[0][i]), str(std[0][i])]]

col_width = max(len(word) for row in out for word in row) + 5
for row in out:
    print ("".join(word.ljust(col_width) for word in row))
