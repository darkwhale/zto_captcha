from image_handler import ImageHandler

import cv2
import os


if __name__ == '__main__':
    for i in range(100, 200):
        image_handler = ImageHandler()
        if image_handler.is_legal():
            print("legal")
            image = image_handler.get_gray_static_image()
            cv2.imwrite(os.path.join("origin", "{}.png".format(str(i))), image)



