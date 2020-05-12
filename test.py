from image_handler import *
# from predict import predict


if __name__ == '__main__':

    image_handler = ImageHandler()

    if image_handler.is_legal():
        print("legal")
        image_handler.save_image("good.{}".format(image_handler.get_suffix()))

        gray_image = image_handler.get_gray_static_image()
        cv2.imwrite("test.png", gray_image)

        image_list = image_handler.generate_uniform_image()
        for index, image in enumerate(image_list):
            cv2.imwrite("{}.png".format(index), image)

        # print(predict(image_list))
