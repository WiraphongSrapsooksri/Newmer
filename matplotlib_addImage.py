import matplotlib.pyplot as plt
import  matplotlib.image as mpimg

img = mpimg.imread('cat-2083492__340.jpg')
img1 = mpimg.imread('image1.jpg')


plt.figure()

plt.subplot(322)
plt.imshow(img)
plt.axis('off')


plt.subplot(323)
plt.imshow(img1)
plt.axis('off')


plt.subplot(324)
plt.imshow(img1)
plt.axis('off')


plt.subplot(325)
plt.imshow(img1)
plt.axis('off')

plt.show()