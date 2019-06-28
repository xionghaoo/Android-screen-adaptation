from shutil import copyfile

import os

from os import listdir
from os.path import isfile, join


SOURCE_DIR = '/Users/xionghao/Documents/icons'
TARGET_DIR = '/Users/xionghao/projects/github/lion/app/src/main/res'
CONFIG_FILE = '/Users/xionghao/Documents/icons/config.txt'
# 将';'号左边的文件名修改成右边的名称
SPLIT_CHARACTER = ';'


def copy_file(source, target):
    copy_file_dpi(source, target, 'xhdpi')
    copy_file_dpi(source, target, 'xxhdpi')
    copy_file_dpi(source, target, 'xxxhdpi')
    # xh_source = join('{0}\\mipmap-xhdpi'.format(SOURCE_DIR), source)
    # xh_target_path = '{0}\\mipmap-xhdpi'.format(TARGET_DIR)
    # if not os.path.exists(xh_target_path):
    #     os.mkdir(xh_target_path)
    # xh_target = join(xh_target_path, target)
    #
    # if isfile(xh_source):
    #     copyfile(xh_source, xh_target)
    #
    # xxh_source = join('{0}\\mipmap-xxhdpi'.format(SOURCE_DIR), source)
    # xxh_target_path = '{0}\\mipmap-xxhdpi'.format(TARGET_DIR)
    # if not os.path.exists(xxh_target_path):
    #     os.mkdir(xxh_target_path)
    # xxh_target = join(xxh_target_path, target)
    # if isfile(xxh_source):
    #     copyfile(xxh_source, xxh_target)


def copy_file_dpi(source, target, dpi):
    dpi_source = join('{0}/mipmap-{1}'.format(SOURCE_DIR, dpi), source)
    target_path = '{0}/mipmap-{1}'.format(TARGET_DIR, dpi)
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    dpi_target = join(target_path, target)

    if isfile(dpi_source):
        copyfile(dpi_source, dpi_target)


def rename_all():
    print("-------copy start-----")
    for line in open(CONFIG_FILE, 'r'):
        names = line.rstrip().split(SPLIT_CHARACTER)
        copy_file(names[0], names[1])
        print('copy file {0}'.format(names[0]))
    print("-------copy end-----")


rename_all()

