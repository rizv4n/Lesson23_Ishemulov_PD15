from tools import foo_regex, read_file as r

d = 'data/apache_logs.txt'
a = 'images\/\w+\.png'

print(list(foo_regex(r(d), a)))
