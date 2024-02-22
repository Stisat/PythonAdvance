from collections import namedtuple
import os
import logging
import argparse

FORMAT = '{levelname} - {asctime}. В модуле создана запись функцией: {funcName}():\n{msg} '
logging.basicConfig(format=FORMAT, style='{', filename='log.txt', filemode='w', encoding='utf-8', level=logging.INFO)

files_t = namedtuple('files_t', 'name, ext_flag, path')


def get_dir_structure(path: str):
    """
    Функция для получения списков файлов и директорий внутри указанного пути path
    в формате X:/Dir/Dir/Dir
    """
    res = []
    for path, file_name, dir_name in os.walk(path):
        res.append((path, file_name, dir_name))
    return res[0]


def set_named(path: str):
    """
     Функция заполняет объекты namedtuple с последующим выводом структуры
    """
    col = list(get_dir_structure(path))
    data_named = []
    curr_dir = str(col[0]).split('/')[-1]
    for name in col[1]:
        data_named.append(files_t(name, 'Dir', curr_dir))
    for name in col[2]:
        parts_name = str(name).split('.')
        data_named.append(files_t(parts_name[0], parts_name[1], curr_dir))
    logging.info('\n'.join(f'{i}' for i in data_named))
    return '\n'.join(f'{i}' for i in data_named)


if __name__ == '__main__':
    pars = argparse.ArgumentParser(description='Получение структуры каталога: ')
    pars.add_argument('path', metavar='P', type=str, help='Enter absolute path to directory')
    arg = pars.parse_args()
    print(set_named(arg.path))
