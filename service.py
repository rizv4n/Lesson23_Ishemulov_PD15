import os
from tools import get_args, read_file, foo_filter, foo_map, foo_unique, foo_sort, foo_limit

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

functions = {
    'filter': foo_filter,
    'map': foo_map,
    'unique': foo_unique,
    'sort': foo_sort,
    'limit': foo_limit
}


def main_func(args):
    cmd_items, value_items = get_args(args)
    if len(cmd_items) > 2:
        return 'Аргументов больше чем 2'
    if args.get('file_name') is None:
        directory = f'{DATA_DIR}/apache_logs.txt'
    else:
        directory = f'{DATA_DIR}/{args.get("file_name")}'
    try:
        cvs = read_file(directory)
    except FileNotFoundError:
        return "Такого файла нет в директории"
    res1 = list(functions[cmd_items['cmd1']](cvs, value_items['value1']))
    try:
        res2 = list(functions[cmd_items['cmd2']](res1, value_items['value2']))
    except KeyError:
        return '<br>'.join(res1)
    return '<br>'.join(res2)
