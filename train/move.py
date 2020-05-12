import os


if __name__ == '__main__':

    with open(os.path.join("cache", "dest.txt"), "r", encoding="utf-8") as reader:
        lines = reader.readlines()

    all_info = "".join([line.strip() for line in lines])

    file_list = [file for file in os.listdir("cache") if file.endswith("png")]

    file_list.sort()

    for char, file_name in zip(all_info, file_list):
        os.rename(os.path.join("cache", file_name), os.path.join("cache", char, file_name))
