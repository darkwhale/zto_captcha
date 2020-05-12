import os
import string


if __name__ == '__main__':

    for i in range(10):
        if not os.path.exists(os.path.join("cache", str(i))):
            os.mkdir(os.path.join("cache", str(i)))

    for i in string.ascii_lowercase:
        if not os.path.exists(os.path.join("cache", str(i))):
            os.mkdir(os.path.join("cache", str(i)))

