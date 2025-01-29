import keras
import matplotlib.pyplot as plt

mnist = keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

plt.imshow(training_images[0],  cmap='gray')
plt.show()
print(training_labels[0])
print(training_images[0])