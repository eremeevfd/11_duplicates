import os
import os.path
from collections import defaultdict


def find_duplicate_files(path):
    file_list = {}
    duplicates = defaultdict(list)
    for root, dirs, files in os.walk(path):
        if '.' not in root:
            for filename in files:
                filepath = os.path.join(root, filename)
                filesize = os.path.getsize(filepath)
                filename = os.path.basename(filepath)
                filename_filesize = filename + ' ' + str(filesize)
                if filename_filesize in file_list:
                    duplicates[filename_filesize].append(filepath)
                    duplicates[filename_filesize].append(file_list.get(filename_filesize))
                file_list[filename_filesize] = filepath
    return duplicates


def print_duplicates(duplicate_files):
    print('This files seem to be duplicates (name, size): ')
    for number, duplicate in enumerate(duplicate_files.values(), start=1):
        print(number, duplicate)

if __name__ == '__main__':
    given_path = input("Enter your directory to find duplicate files: ")
    if os.path.exists(given_path):
        duplicate_files = find_duplicate_files(given_path)
        print_duplicates(duplicate_files)
