import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

model = tf.keras.models.load_model('handwritten.keras')

image_number = 1
while os.path.isfile(f'digits/digit{image_number}.png'):
    try:
        img = cv2.imread(f'digits/digit{image_number}.png')[:,:,0]

        img = cv2.resize(img, (28,28))
        img = np.invert(img)

        img = img / 255.0
        img = np.array([img])

        prediction = model.predict(img)

        print(f'The digit is probably a {np.argmax(prediction)}')

        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()

    except:
        print('Error !!')

    finally:
        image_number += 1
