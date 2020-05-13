import os
import shutil


if __name__ == '__main__':

    dirs = "png"

    with open(os.path.join(dirs, "dest.txt"), "r", encoding="utf-8") as reader:
        lines = reader.readlines()

    all_info = "".join([line.strip() for line in lines])

    file_list = [file for file in os.listdir(dirs) if file.endswith("png")]

    file_list.sort()

    for char, file_name in zip(all_info, file_list):
        # print(char, file_name)
        # shutil.copy(os.path.join(dirs, file_name), os.path.join(dirs, char, file_name))
        shutil.copy(os.path.join(dirs, file_name), os.path.join("cache", char, file_name))
