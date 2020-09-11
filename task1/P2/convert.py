import numpy as np

data=np.genfromtxt('mumbai_data.csv',delimiter=',', dtype= str)
label=data[0:1,1:]
value=np.genfromtxt('mumbai_data.csv',delimiter=',')
value=value[1:,1:]
label[0][0]='Tests per Million'
label[0][1]='Test Positivity rate'
value[:, 1]=value[:, 1]/value[:, 0]
value[:, 0]=value[:, 0]/20.4
value[:, 0]=np.around(value[:, 0], decimals=0)
value[:, 1]=np.around(value[:, 1], decimals=3)

transformed=np.append(label, value, axis=0)
data[:, 1:]=transformed
np.savetxt('transformed.csv', data, delimiter=',',fmt='%s')

std=np.around(np.std(value, axis=0, keepdims=True), decimals=3)
mean=np.around(np.mean(value, axis=0, keepdims=True), decimals=3)


out=[['Field', 'Mean', 'Std. Dev.']]
c=label.shape[1]
for i in range(c):
	out=out + [[label[0][i], str(mean[0][i]), str(std[0][i])]]

col_width = max(len(word) for row in out for word in row)+5
for row in out:
    print ("".join(word.ljust(col_width) for word in row))