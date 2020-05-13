import os
import string


if __name__ == '__main__':
    
    dirs = "gif"

    for i in range(10):
        if not os.path.exists(os.path.join(dirs, str(i))):
            os.mkdir(os.path.join(dirs, str(i)))

    for i in string.ascii_lowercase:
        if not os.path.exists(os.path.join(dirs, str(i))):
            os.mkdir(os.path.join(dirs, str(i)))

