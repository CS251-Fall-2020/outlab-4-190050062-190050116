import numpy as np

label = np.genfromtxt('mumbai_data.csv', delimiter=',', dtype=str)
label = label[0:1, 1:]
value = np.genfromtxt('mumbai_data.csv', delimiter=',')
value = value[1:, 1:]

std = np.std(value, axis=0, keepdims=True)
mean = np.mean(value, axis=0, keepdims=True)

out = [['Field', 'Mean', 'Std. Dev.']]
c = label.shape[1]
for i in range(c):
    tr_mean = np.format_float_positional(
        mean[0][i], precision=3, unique=False)
    tr_std = np.format_float_positional(
        std[0][i], precision=3, unique=False)
    out = out + [[label[0][i], str(tr_mean), str(tr_std)]]

col_width = max(len(word) for row in out for word in row) + 5
for row in out:
    print("".join(word.ljust(col_width) for word in row))
