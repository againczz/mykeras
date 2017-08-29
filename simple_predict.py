

# Modify 'test1.jpg' and 'test2.jpg' to the images you want to predict on
import os
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# dimensions of our images
img_width, img_height = 32, 32

# load the model we saved
model = load_model('models/cifar10.h5')
# model.compile(loss='binary_crossentropy',
#               optimizer='rmsprop',
#               metrics=['accuracy'])

# predicting images
for root,dir,files in os.walk('D:\\work\\tfwork\\image\\val\\other'):
    for image_name in files:
        image_file = os.path.join(root,image_name)
        img = image.load_img(image_file, target_size=(img_width, img_height))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        images = np.vstack([x])
        classes = model.predict_classes(images)
        print(classes)

# # predicting multiple images at once
# img = image.load_img('test2.jpg', target_size=(img_width, img_height))
# y = image.img_to_array(img)
# y = np.expand_dims(y, axis=0)
#
# # pass the list of multiple images np.vstack()
# images = np.vstack([x, y])
# classes = model.predict_classes(images, batch_size=10)
#
# # print the classes, the images belong to
# print
# classes
# print
# classes[0]
# print
# classes[0][0]