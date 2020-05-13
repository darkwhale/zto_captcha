import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Activation, Flatten, BatchNormalization
import os

from config import feature_str
from model import build_model


model = build_model(os.path.join("train", "model.h5"))


def predict(image_list):
    image_list = [np.expand_dims(sub_image, axis=-1) for sub_image in image_list]

    return "".join([feature_str[index] for index in model.predict_classes(np.array(image_list))])