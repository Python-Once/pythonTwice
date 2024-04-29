import os, shutil

# path = "/Users/chunheiyue/Documents/tmp/"
# folder_names = 'by_name'
# file_name = os.listdir(path)


def get_name(path, file):
    name = None
    if os.path.isfile(path+file) and file!='.DS_Store':
        stripped = file.split('.')
        name = stripped[0]
    return name

def set_occurance(path, file, occurance):
    name = get_name(path, file)
    if name is not None:
        if name not in occurance:
            occurance[name] = 1
        else:
            occurance[name] += 1

def move_files_byname(path, file, folder_names, key, element):
    name = get_name(path, file)
    if name is not None:
        if name == key and element > 1:
                if not os.path.exists(path + folder_names + '/' + name):
                    os.makedirs(path + folder_names + '/' + name)
                shutil.move(path + file, os.path.join(path, folder_names + '/' + name, file))

def create_dir_byname(path, folder_names):
    if not os.path.exists(path + folder_names):
        os.makedirs(path + folder_names)


def namefunc(path):
    folder_names = 'by_name'
    file_name = os.listdir(path)
    occurance = {}

    create_dir_byname(path, folder_names)

    for file in file_name:
        set_occurance(path, file, occurance)

    for key, element in occurance.items():
        for file in file_name:
            move_files_byname(path, file, folder_names, key, element)