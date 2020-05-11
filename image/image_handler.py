import requests
import json
import base64

from config import zto_image_url


class ImageHandler(object):
    def __init__(self):
        # todo 异常检测
        self.image_content = requests.post(zto_image_url, timeout=3)

        self.origin_image_dict = self.image_content.text

        base_dict = json.loads(self.origin_image_dict)
        self.image_base64_str = base_dict.get("result").get("image")
        self.id = base_dict.get("id")

        base64_index = self.image_base64_str.find("base64")
        self.fore_info, self.image_info = self.image_base64_str[: base64_index], \
                                          self.image_base64_str[base64_index + 7:]

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

    def save_image(self, file_name):
        with open("{}.{}".format(file_name, self.get_suffix()), "wb") as writer:
            writer.write(base64.b64decode(self.image_info))

