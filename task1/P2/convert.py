import numpy as np

data = np.genfromtxt('mumbai_data.csv', delimiter=',', dtype=str)
data = np.char.ljust(data, 25)
label = data[0:1, 1:]
value = np.genfromtxt('mumbai_data.csv', delimiter=',')
value = value[1:, 1:]
label[0][0] = 'Tests per Million'
label[0][1] = 'Test Positivity rate'
value[:, 1] = value[:, 1] / value[:, 0]
value[:, 0] = value[:, 0] / 20.4
value[:, 0] = np.around(value[:, 0], decimals=0)
value[:, 1] = np.around(value[:, 1], decimals=3)

transformed = np.append(label, value, axis=0)

data[:, 1:] = transformed
np.savetxt('transformed.csv', data, delimiter=',', fmt='%s')
