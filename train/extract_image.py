from image_handler import ImageHandler
from config import cache_dir
from region import *

import cv2
import os


if __name__ == '__main__':

    image_index = 400

    for i in range(100):
        image_handler = ImageHandler()
        if image_handler.is_legal():
            print("legal")
            image_list = image_handler.generate_uniform_image()
            for image in image_list:
                cv2.imwrite(os.path.join(cache_dir, "{}.png".format(str(image_index))), image)
                image_index += 1
        else:
            print("被墙了")
