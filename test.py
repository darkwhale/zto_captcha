from image_handler import *
import base64
import json


if __name__ == '__main__':

    image_handler = ImageHandler()

    print(image_handler.get_origin_content())
    print(image_handler.get_fore_info())
    print(image_handler.get_image_info())
    print(image_handler.get_suffix())
    print(image_handler.get_id())
    image_handler.save_image("ceshi")