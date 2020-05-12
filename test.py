from image_handler import *
from predict import predict


if __name__ == '__main__':

    image_handler = ImageHandler()

    if image_handler.is_legal():
        print("legal")
        image_handler.save_image("good.{}".format(image_handler.get_suffix()))

        image_list = image_handler.generate_uniform_image()

        print(predict(image_list))
