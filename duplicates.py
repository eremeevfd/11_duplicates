import os
import os.path
from collections import defaultdict


def find_duplicate_files(path):
    file_list = {}
    duplicates = defaultdict(list)
    for root, dirs, files in os.walk(path):
        files = [file for file in files if not file[0] == '.']
        try:
            for filename in files:
                filepath = os.path.join(root, filename)
                filesize = os.path.getsize(filepath)
                filename = os.path.basename(filepath)
                filename_filesize = '{filename} {filesize}'.format(filename=filename, filesize=filesize)
                if filename_filesize in file_list:
                    duplicates[filename_filesize].append(filepath)
                    duplicates[filename_filesize].append(file_list.get(filename_filesize))
                file_list[filename_filesize] = filepath
        except FileNotFoundError:
            pass
    return duplicates


def print_duplicates(duplicate_files):
    print('This files seem to be duplicates (name, size): ')
    for duplicate_group in duplicate_files.values():
        print('--------')
        for duplicate_file in duplicate_group:
            print(duplicate_file)


if __name__ == '__main__':
    given_path = input("Enter your directory to find duplicate files: ")
    if os.path.exists(given_path):
        duplicate_files = find_duplicate_files(given_path)
        print_duplicates(duplicate_files)
