def get_args(args):
    cmd_items = {i: args.get(i) for i in args if 'cmd' in i}
    value_items = {i: args.get(i) for i in args if 'value' in i}
    return cmd_items, value_items


def read_file(direct):
    with open(direct, "r") as f:
        return iter(f.read().split('\n'))


def foo_filter(data, value):
    res = filter(lambda v: value in v, data)
    return res


def foo_map(data, value=None):
    res = map(lambda v: v.split('-')[0].replace(' ', ''), data)
    if value == '0' or value is None:
        return res
    else:
        res = map(lambda v: v.split('.')[int(value)], res)
        return res


def foo_unique(data, value=None):
    res = set(data)
    return res


def foo_sort(data, value='ask'):
    if value == 'ask' or None:
        res = sorted(data)
        return res
    elif value == 'desk':
        res = sorted(data, reverse=True)
        return res


def foo_limit(data, value):
    return data[:int(value)]
