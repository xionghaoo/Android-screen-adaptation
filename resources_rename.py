from shutil import copyfile

import os

from os import listdir
from os.path import isfile, join


SOURCE_DIR = 'I:\\python\\source'
TARGET_DIR = 'I:\\python\\target'
CONFIG_FILE = 'config.txt'
SPLIT_CHARACTER = ';'


def copy_file(source, target):
    xh_source = join('{0}\\drawable-xhdpi'.format(SOURCE_DIR), source)
    xh_target_path = '{0}\\drawable-xhdpi'.format(TARGET_DIR)
    if not os.path.exists(xh_target_path):
        os.mkdir(xh_target_path)
    xh_target = join(xh_target_path, target)

    if isfile(xh_source):
        copyfile(xh_source, xh_target)

    xxh_source = join('{0}\\drawable-xxhdpi'.format(SOURCE_DIR), source)
    xxh_target_path = '{0}\\drawable-xxhdpi'.format(TARGET_DIR)
    if not os.path.exists(xxh_target_path):
        os.mkdir(xxh_target_path)
    xxh_target = join(xxh_target_path, target)
    if isfile(xxh_source):
        copyfile(xxh_source, xxh_target)


def rename_all():
    for line in open(CONFIG_FILE, 'r'):
        names = line.rstrip().split(SPLIT_CHARACTER)
        copy_file(names[0], names[1])


rename_all()

