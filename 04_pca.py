from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import joblib
import numpy as np

data = np.load('data/data_normalized_100x100.npz')
print(data.files)
x = data['arr_0']
y = data['arr_1']

pca = PCA(n_components=None, whiten=True)
x_pca = pca.fit_transform(x)
explained_variance_ratio = pca.explained_variance_ratio_
explained_variance_ratio_cumsum = np.cumsum(explained_variance_ratio)

# Ploting results
plt.plot(explained_variance_ratio_cumsum, 'r>--')
plt.show()

# Finding how much features we need for 85% of the explained variance
arg = np.argwhere(explained_variance_ratio_cumsum > 0.85)[0]
print('Features: ', arg, '- Explained Variance: ', explained_variance_ratio_cumsum[arg])

# Applying pca to extract features and reverting to the original size
pca = PCA(n_components=50, whiten=True)
x_pca_feat = pca.fit_transform(x)
joblib.dump(pca, 'model/pcafeat_model.joblib')
np.save('data/data_pcafeat_100x100.npy', x_pca_feat)

# Reverting state
x_pca_inv = pca.inverse_transform(x_pca_feat)

fig, ax = plt.subplots(1,2)
ax[0].imshow(x[0].reshape((100,100)), cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(x_pca_inv[0].reshape((100,100)), cmap='gray')
ax[1].set_title('PCA inv')
plt.tight_layout()
plt.show()
