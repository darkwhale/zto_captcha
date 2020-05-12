from image_handler import *
import base64
import json
import os
from PIL import Image, ImageSequence
import numpy as np
import cv2
from functools import reduce


if __name__ == '__main__':

    image_handler = ImageHandler()

    if image_handler.is_legal():
        print("legal")
        # image_handler.save_image()
        image_handler.save_image("good.{}".format(image_handler.get_suffix()))

        # gray_image = image_handler.get_gray_static_image()
        # cv2.imwrite("good.png", gray_image)

        image_list = image_handler.generate_uniform_image()

        for index, image in enumerate(image_list):
            cv2.imwrite("{}.png".format(str(index).zfill(3)), image)