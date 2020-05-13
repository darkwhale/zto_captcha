from image_handler import *


if __name__ == '__main__':

    image_handler = ImageHandler()

    if image_handler.is_legal():
        print("legal")
        image_handler.save_image("good.{}".format(image_handler.get_suffix()))

        image_list = image_handler.generate_uniform_image()
        for index, image in enumerate(image_list):
            cv2.imwrite("{}.png".format(index), image)

        print(image_handler.get_predict())
