from image_handler import *
import base64
import json
import os
from PIL import Image, ImageSequence
import numpy as np
import cv2
from functools import reduce


if __name__ == '__main__':

    image_handler = ImageHandler("001")
    print(image_handler.is_legal())
    print(image_handler.get_suffix())

    image_handler.save_image()

    image = image_handler.get_gray_static_image()
    cv2.imwrite("good.png", image)