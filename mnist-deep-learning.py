from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 1. Prepare the Data
from keras.utils import to_categorical
train_images = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 2. Set up network architecture
from keras import models, layers
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# 3/4. Pick Optimizer and Loss
network.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# 5. Measure on test
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
