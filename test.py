from itertools import groupby
file_path = "C:\\work\\gitblog\\blog\\2018-11-02 16-22-00=Программирование=О гитхаб"

def to_description(path):
    try:
        fp = open(path+'/text.md', encoding="utf8")
        for i, line in enumerate(fp):
            if i == 0:
                return line.splitlines()[0]
    except BaseException as trabl:
        # TODO записать ошибку в лог
        return False

print(to_description(file_path))