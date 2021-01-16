import os
import sys

platformOS = sys.platform

if platformOS == 'linux':
    pat = '/home/drak/jallery'
elif platformOS == 'win32':
    pat = 'c:/'

dir_list = []
file_list = []
pict_list = []
template = 'jpg'
pic = str


def what_is_what(pat):
    try:
        os.chdir(pat)
        ListOfAll = list(os.listdir())
        for count in range(0, len(ListOfAll)):
            if os.path.isfile(ListOfAll[count]):
                file_list.append(ListOfAll[count])
            else:
                dir_list.append(ListOfAll[count])
    except:
        print('ERROR - Brak Dostępu')


def change_path():
    tmpppath = pat
    newpath = pat
    try:
        os.chdir(pat + '/' + dir_list[count])
    except:
        print('Error - brak dostepu')


def find_pic(ext, files_list):
    count = 0

    for count in range(0, len(files_list)):
        if files_list[count].split('.')[-1] == ext:
            pict_list.append(os.getcwd() + '/' + files_list[count])
    return pict_list


def gen_path():

    for count in range(0,len(pict_list)):
        return pict_list[count]


def give_me_a_pic_path():
    what_is_what('/home/drak/')
    find_pic(template, file_list)
    x = gen_path()
    # for _ in range(0,len(pict_list)):
    count = 0
    while count != len(pict_list):
        x = pict_list[count]
        count += 1
        yield x

