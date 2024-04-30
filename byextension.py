import os, shutil
# path = "/Users/chunheiyue/Documents/tmp/"
# folder_name = 'by_extension'
# file_name = os.listdir(path)
# extenison_names = ['doc files', 'pdf files', 'image files', 'text files']

# def create_dir(path, folder_name, extenison_name):
#     if not os.path.exists(path + folder_name + '/' + extenison_name):
#         os.makedirs(path + folder_name + '/' + extenison_name)

# def move_files(path, folder_name, file):
#     if '.doc' in file and not os.path.exists(path + folder_name + '/' + 'doc files/' + file):
#         shutil.move(path + file, path + folder_name + '/' + 'doc files/' + file)  
#     elif '.pdf' in file and not os.path.exists(path + folder_name + '/' + 'pdf files/' + file):
#         shutil.move(path + file, path + folder_name + '/' + 'pdf files/' + file)
#     elif '.png' in file and not os.path.exists(path + folder_name + '/' + 'image files/' + file):
#         shutil.move(path + file, path + folder_name + '/' + 'image files/' + file)

def move_files(path, folder_name, file):
    if file == '.DS_Store':
        return
    if not os.path.isfile(os.path.join(path, file)):
        return
    filename, extension = os.path.splitext(file)
    if not extension:
        return  
    extension = extension[1:]
    destination_folder = os.path.join(path, folder_name, extension)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))

def extensionfunc(path):
    folder_name = 'by_extension'
    file_name = os.listdir(path)
    # extenison_names = ['doc files', 'pdf files', 'image files', 'text files']

    # for loop in range(len(extenison_names)):
    #     create_dir(path, folder_name, extenison_names[loop])

    for file in file_name:
        move_files(path, folder_name, file)
