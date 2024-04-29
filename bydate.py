# import os, shutil, platform, datetime
# folder_names = 'by_date'
# file_name = os.listdir(path)

import os, glob, time, shutil, platform
 
# path = "C:/test/"

# path = "/Users/chunheiyue/Documents/tmp/"


def datefunc(path):

    filenames = glob.glob(path+'*')

    for file in filenames:

        ctime = time.ctime(os.path.getctime(file))
        tobj = time.strptime(ctime)
        Tstamp = time.strftime("%m %Y", tobj)

        if platform.system() == 'Windows':
            ctime = time.ctime(os.path.getctime(file))
            tobj = time.strptime(ctime)
            Tstamp = time.strftime("%m %Y", tobj)
        else:
            stat = os.stat(file)
            birth_time = stat.st_birthtime
            Tstamp = time.strftime("%m %Y", time.localtime(birth_time))
                    
        directory = os.path.join(path, 'by_date', Tstamp)

        if not os.path.exists(directory) and file!='.DS_Store' and os.path.isfile(file):
            os.makedirs(directory)
    
        if os.path.isfile(file):
            shutil.move(file, directory)        


# def creation_date(path_to_file):
#     if platform.system() == 'Windows':
#         return os.path.getctime(path_to_file)
#     else:
#         stat = os.stat(path_to_file)
#         return stat.st_birthtime

# def get_year_month(time):
#     return str(datetime.datetime.fromtimestamp(time).year), str(datetime.datetime.fromtimestamp(time).month)

# def move_files(path, file, folder_names, year, month):
#     if not os.path.exists(path + folder_names + '/' + year + '-' + month):
#         os.makedirs(path + folder_names + '/' + year + '-' + month)
#     if not os.path.exists(path + folder_names + '/' + year + '-' + month + '/' + file):
#         shutil.move(path + file, os.path.join(path + folder_names + '/' + year + '-' + month, file))

# for file in file_name:
#     if os.path.isfile(path+file) and file!='.DS_Store':
#         date = creation_date(path+file)
#         year, month = get_year_month(date)
#         move_files(path, file, folder_names, year, month)




