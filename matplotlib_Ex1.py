import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 20)
f = np.arange(-10, 30)
g = np.sin(np.arange(0, 10, 0.01) * 2) * 30
# g = x-3
plt.plot(x, f, '-')
plt.plot(x, g, '-')

idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
plt.plot(x[idx], f[idx], 'ro')
plt.show()