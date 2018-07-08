# 1、请将该程序放到app/src/main/res文件目录下运行
# 2、该程序将layout下面每个xml文件中dp和sp的值修改为@dimen/x[number]dp格式，
#   如15dp修改为@dimen/x15dp，16sp修改为@dimen/x16sp

from shutil import copyfile

import re
import os

from os import listdir
from os.path import isfile, join

import codecs

MODIFY_FOLDER_NAME = 'layout'


def modify_dimen(file_name):
    copy_file_name = file_name + '-copy'
    copyfile(file_name, copy_file_name)

    fin = codecs.open(copy_file_name, 'r', encoding='utf-8')
    fout = codecs.open(file_name, 'w', encoding='utf-8')

    for line in fin:
        new_line = line
        match = re.match('.*["]([\\d]+)[ds]p["].*', line)
        if match:
            value = match.group(1)
            if int(value) > 1:
                # 大于1dp(sp)的才替换
                new_line = line.replace(value, '@dimen/x{0}'.format(value))
        fout.write(new_line)

    fin.close()
    fout.close()

    os.remove(copy_file_name)


def modify_all_dimens(path):
    file_list = [f for f in listdir(path) if isfile(join(path, f))]
    for f in file_list:
        modify_dimen(join(path, f))
        print('modify file: ' + join(path, f))


modify_all_dimens(MODIFY_FOLDER_NAME)


