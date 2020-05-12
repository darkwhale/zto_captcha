from PIL import Image
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':
    file_path = sys.argv[1]

    image = Image.open(file_path)
    plt.figure("test")
    plt.imshow(image)
    plt.show()