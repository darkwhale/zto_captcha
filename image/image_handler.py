import requests
import json
import base64
import os
from PIL import Image, ImageSequence
import numpy as np
import cv2
from functools import reduce

from config import zto_image_url, cache_dir
from exception import RequestException

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)


def get_url():
    try_num = 5
    while try_num:
        try:
            content = requests.post(zto_image_url, timeout=3)
            if content.status_code == 200:
                return content
        finally:
            try_num -= 1

    raise RequestException("request异常")


class ImageHandler(object):
    def __init__(self,
                 cache_file_name=None):

        self.status = None

        # noinspection PyBroadException
        try:
            self.image_content = get_url()

            self.cache_file_name = "0" if cache_file_name is None else str(cache_file_name)

            self.origin_image_dict = self.image_content.text

            base_dict = json.loads(self.origin_image_dict)
            self.image_base64_str = base_dict.get("result").get("image")
            self.id = base_dict.get("id")

            base64_index = self.image_base64_str.find("base64")
            self.fore_info, self.image_info = self.image_base64_str[: base64_index], \
                                              self.image_base64_str[base64_index + 7:]

            self.status = 0
        except RequestException:
            self.status = 1
        except Exception:
            self.status = 2

    def is_legal(self):
        return self.status == 0

    def get_origin_content(self):
        return self.origin_image_dict

    def get_suffix(self):
        return "png" if "png" in self.fore_info else "gif"

    def get_fore_info(self):
        return self.fore_info

    def get_image_info(self):
        return self.image_info

    def get_id(self):
        return self.id

    def save_image(self):
        with open(os.path.join(cache_dir, "{}.{}".format(self.cache_file_name, self.get_suffix())), "wb") as writer:
            writer.write(base64.b64decode(self.image_info))

    def get_image_name(self):
        return os.path.join(cache_dir, "{}.{}".format(self.cache_file_name, self.get_suffix()))

    def get_gray_static_image(self):
        # 1.保存图像，2.读取图像，3.判断为png还是gif，4.处理返回
        # 先保存图片
        self.save_image()

        file_path = self.get_image_name()

        image = Image.open(file_path)

        np_merge = None

        # png直接返回灰度图像，gif读取帧然后合并图像
        if self.get_suffix() == "png":
            np_list = np.asarray(image)
            np_merge = cv2.cvtColor(np_list, cv2.COLOR_BGR2GRAY)

        else:
            np_list = list()
            for index, image_frame in enumerate(ImageSequence.Iterator(image)):
                np_list.append(np.asarray(image_frame))

            np_merge = reduce(np.minimum, np_list)

        return np_merge


