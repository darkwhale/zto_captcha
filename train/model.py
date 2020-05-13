from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D
import os
import numpy as np
from keras.optimizers import  Adam
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import cv2
from config import *


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

    model.add(Conv2D(64, (3, 3)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(256, activation='relu'))
    model.add(Dense(32, activation='softmax'))

    if weight_path is not None:
        model.load_weights(weight_path)

    return model


def lr_rate(epoch):
    """Learning Rate Schedule

    Learning rate is scheduled to be reduced after 10, 20, 30, 40 epochs.
    Called automatically every epoch as part of callbacks during training.

    # Arguments
        epoch (int): The number of epochs

    # Returns
        lr (float32): learning rate
    """
    lr = 1e-2
    if epoch > 18:
        lr *= 0.5e-3
    elif epoch > 15:
        lr *= 1e-3
    elif epoch > 10:
        lr *= 1e-2
    elif epoch > 5:
        lr *= 1e-1
    print('Learning rate: ', lr)
    return lr


# 获取文件夹下所有的文件列表；
def get_file_list(file_dir):
    file_list = []

    for root, dirs, files in os.walk(file_dir):
        for name in files:
            file_list.append(os.path.join(root, name))

    file_list.sort()

    return file_list


def get_feature_dict():
    return dict([(feature, index) for index, feature in enumerate(feature_str)])


base_feature_dict = get_feature_dict()


if __name__ == '__main__':

    file_list = get_file_list("cache")

    train_x, train_y = [], []

    for file in file_list:
        image = np.expand_dims(cv2.imread(file, 0), axis=-1)
        label = np_utils.to_categorical(base_feature_dict[os.path.basename(os.path.dirname(file))], 32)
        train_x.append(image)
        train_y.append(label)

    train_x, train_y = np.array(train_x), np.array(train_y)
    x_train, x_valid, y_train, y_valid = train_test_split(train_x, train_y, test_size=0.2)

    cnn_model = build_model()
    cnn_model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=lr_rate(0)),
                      metrics=['accuracy'])

    cnn_model.summary()

    cnn_model.fit(x_train, y_train, validation_data=(x_valid, y_valid), verbose=1, batch_size=64, epochs=30)

    scores = cnn_model.evaluate(x_valid, y_valid, verbose=1)

    cnn_model.save_weights("model.h5")

