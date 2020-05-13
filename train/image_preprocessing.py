import cv2
import os
import numpy as np

from region_value import *

new_dir = "new_cache"

if not os.path.exists(new_dir):
    os.mkdir(new_dir)


if __name__ == '__main__':

    for sub_dir in os.listdir("cache"):
        sub_dir_path = os.path.join("cache", sub_dir)

        for file in os.listdir(sub_dir_path):
            image = cv2.imread(os.path.join(sub_dir_path, file), 0)

            avg = np.mean(image[:, :])
            std = np.std(image[:, :])
            if std < 50:
                width, height = image.shape
                point_dict = dict()

                for i in range(width):
                    for j in range(height):
                        if image[i, j] > 10:
                            point_dict[Point(i, j)] = image[i, j]
                region_value = RegionValue(point_dict)
                new_image = region_value.generate_image()
                cv2.imwrite(os.path.join("new_cache", sub_dir, file), new_image)

                new_images = region_value.generate_images()
                for index, sub_image in enumerate(new_images):
                    cv2.imwrite(os.path.join("new_cache", sub_dir, "{}{}".format(index, file)), sub_image)
