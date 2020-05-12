from image_handler import ImageHandler
from config import cache_dir

import cv2
import os


if __name__ == '__main__':

    image_index = 100

    for i in range(20):
        image_handler = ImageHandler()
        if image_handler.is_legal():
            print("legal")
            image_list = image_handler.generate_uniform_image()
            image = image_handler.get_gray_static_image()
            cv2.imwrite(os.path.join("origin", "{}.png".format(str(i))), image)
            for image in image_list:
                cv2.imwrite(os.path.join(cache_dir, "{}.png".format(str(image_index))), image)
                image_index += 1
        else:
            print("被墙了")
