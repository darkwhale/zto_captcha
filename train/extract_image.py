from image_handler import ImageHandler

import cv2
import os
import time


if __name__ == '__main__':

    image_index = len(os.listdir(os.path.join("cache")))

    while True:
        for _ in range(10):
            image_handler = ImageHandler()
            if image_handler.is_legal():
                print("legal")

                image_list = image_handler.generate_uniform_image()
                image = image_handler.get_gray_static_image()
                cv2.imwrite(os.path.join("origin", "{}.png".format(str(image_index).zfill(5))), image)
                image_index += 1

                if image_handler.get_suffix() == "png":
                    dest_dir = "png"
                else:
                    dest_dir = "gif"
                for image in image_list:
                    cv2.imwrite(os.path.join(dest_dir, "{}.png".format(str(image_index).zfill(4))), image)
                    image_index += 1
            else:
                print("被墙了")

        time.sleep(200)