# 1、请将该程序放到app/src/main/res文件目录下运行
# 2、该程序会自动生成xxxhdpi、xxhdpi、xhdpi的dimens文件

import os

# UI设计以iPhone plus的屏幕为标准设计，
# 换算成Android屏幕，比较接近的为2K屏(xxxhdpi屏幕)
UI_SCREEN_SCALE = 3.5
UI_SCREEN_WIDTH = 1440.0

# 1K屏(xxhdpi屏幕)，市面上大部分的手机都采用这种屏幕
XXHDPI_SCREEN_SCALE = 3.0
XXHDPI_SCREEN_WIDTH = 1080.0

XHDPI_SCREEN_SCALE = 2.0
XHDPI_SCREEN_WIDTH = 720.0

# 文件夹名称
dimen_type_xxxhdpi = 'values-xxxhdpi'
dimen_type_xxhdpi = 'values-xxhdpi'
dimen_type_xhdpi = 'values-xhdpi'

OUTPUT_FILE_NAME = 'values-constants.xml'

SP_START = 1
SP_END = 61
DP_START = 1
DP_END = 501


def create_file(dimen_type):
    new_path = r'{0}'.format(dimen_type)
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    file = open('{0}/{1}'.format(dimen_type, OUTPUT_FILE_NAME), 'w')

    file.write('<resources>\n')

    # create sp line
    file.write('\t<!--sp dimension-->\n')
    for sp in range(SP_START, SP_END):
        file.write('\t<dimen name="x{0}sp">{1}sp</dimen>\n'.format(str(sp), get_screen_dimension(sp, dimen_type)))

    # create dp line
    file.write('\n\t<!--dp dimension-->\n')
    for dp in range(DP_START, DP_END):
        file.write('\t<dimen name="x{0}dp">{1}dp</dimen>\n'.format(str(dp), get_screen_dimension(dp, dimen_type)))

    file.write('</resources>\n')
    file.close()


def get_screen_dimension(size, dimen_type):
    if dimen_type == dimen_type_xxxhdpi:
        return size
    elif dimen_type == dimen_type_xxhdpi:
        return round(size * UI_SCREEN_SCALE / UI_SCREEN_WIDTH * XXHDPI_SCREEN_WIDTH / XXHDPI_SCREEN_SCALE, 2)
    elif dimen_type == dimen_type_xhdpi:
        return round(size * UI_SCREEN_SCALE / UI_SCREEN_WIDTH * XHDPI_SCREEN_WIDTH / XHDPI_SCREEN_SCALE, 2)
    else:
        return 0


create_file(dimen_type_xxxhdpi)
create_file(dimen_type_xxhdpi)
create_file(dimen_type_xhdpi)

