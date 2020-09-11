from PIL import Image
import scipy.cluster
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True)
ap.add_argument("--k", required=True)
ap.add_argument("--output", required=False)
args = vars(ap.parse_args())

img=np.array(Image.open(str(args['input'])), np.float)
M=img.reshape((img.shape[0]*img.shape[1], img.shape[2]))

centroid, label=scipy.cluster.vq.kmeans2(M, int(args['k']), iter=100, minit='++', check_finite=True)
m=M.shape[0]
for i in range(m):
	M[i, :]=centroid[label[i], :]

M=M.reshape((img.shape[0], img.shape[1], img.shape[2]))
new_image = Image.fromarray(M.astype('uint8'), 'RGB')
new_image.save(str(args['output']))