import numpy as np

data=np.genfromtxt('mumbai_data.csv',delimiter=',', dtype=str)
data1=np.genfromtxt('mumbai_data.csv',delimiter=',')
data2=np.genfromtxt('mumbai_unlock.csv',delimiter=',')
value1=data1[1:, 1:]
value2=data2[1:, 1:]
label=np.array([['Infected(UnLock)', 'Infected(Lock)', 'Positivity Rate(Lock)', 'Positivity Rate(UnLock)']])
merge=np.zeros((8,5), dtype=object)
merge[:,0]=data[:,0]
merge[0,1:]=label

merge[1:,1]=value2[:,1]
value2[:, 1]=value2[:, 1]/value2[:, 0]
value2[:, 1]=np.around(value2[:, 1], decimals=3)
merge[1:, 4]=value2[:,1]

merge[1:,2]=value1[:,1]
value1[:, 1]=value1[:, 1]/value1[:, 0]
value1[:, 1]=np.around(value1[:, 1], decimals=3)
merge[1:, 3]=value1[:,1]
np.savetxt('info_combine.csv', merge, delimiter=',',fmt='%s')
