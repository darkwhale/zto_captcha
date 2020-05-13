from image_handler import *
from predict import predict
import cv2


def read_image(image_name):
    image = cv2.imread(image_name, 0)
    return np.array(image)


if __name__ == '__main__':

    image_1 = read_image("2148.png")
    image_2 = read_image("2693.png")
    image_3 = read_image("2746.png")
    image_4 = read_image("0.png")

    image_list = [image_1, image_2, image_3, image_4]
    print(predict(np.array(image_list)))
