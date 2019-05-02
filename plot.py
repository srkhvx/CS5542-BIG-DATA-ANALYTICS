import numpy as np
from sklearn.manifold import TSNE
import pickle
import matplotlib.cm as cm
import matplotlib.pyplot as plt


with open('features.pkl', 'rb') as f:
    data = pickle.load(f)



#plt.imshow(data[0].reshape((28, 28)), cmap=cm.Greys_r)
#plt.show()
temp=list(data.values())

print(len(temp))
np_array=np.array(temp[0][0])
td_array=np.reshape(np_array, (-1, 2048))
#X = td_array.transpose(2,0,1).reshape(3,-1)
X_embedded = TSNE(n_components=2).fit_transform(td_array)
print(X_embedded)

import matplotlib.pyplot as plt
xyz=X_embedded
plt.scatter(xyz[:,0], xyz[:,1])