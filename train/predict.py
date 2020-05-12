import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Flatten, BatchNormalization
import os

from config import feature_str


def build_model(weight_path=None):
    model = Sequential()
    model.add(Conv2D(16, (3, 3), padding='same', input_shape=(36, 36, 1)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(128, activation='relu'))
    model.add(Dense(32, activation='softmax'))

    if weight_path:
        model.load_weights(weight_path)

    return model


model = build_model(os.path.join("train", "model.h5"))


def predict(image_list):
    image_list = [np.expand_dims(sub_image, axis=-1) for sub_image in image_list]

    return "".join([feature_str[index] for index in model.predict_classes(np.array(image_list))])