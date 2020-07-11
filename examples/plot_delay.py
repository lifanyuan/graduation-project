import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.8, 3.2, 0.2)
y = np.array([1.335e9, 1.409e9, 1.560e9, 1.577e9, 1.645e9, 1.630e9, 1.621e9])
plt.plot(x, y, marker='D', ls=':')
plt.xlabel('delay tolerance/s')
plt.ylabel('computation rate')
plt.show()
