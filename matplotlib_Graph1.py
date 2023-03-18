import matplotlib.pyplot as plt
import numpy as np



a = np.arange(0,5,0.5)
plt.plot(a,a,'r-',label='Fish')
plt.plot(a,a**2,'g^',label='Dog')
plt.plot(a,a**3,'bs',label='Cat')

plt.legend()

# plt.plot([1,5,2,5,3])
# plt.ylabel('Y-axis')
# plt.xlabel('X-axis')
plt.show()