import sys


def getTxt(file_name):
    # 返回一个二维数组
    res = [] # 开辟一块空间
    path = sys.path[0]
    # print(path)
    with open(file_name, 'r', encoding='utf-8') as fp:
        lines = fp.readlines() # 读取全部内容，返回的一个list。每一行，就是一个元素
        i = 1
        length = len(lines)
        while i < length:
            tmp = lines[i].split(",")
            value = []
            for val in tmp:
                if val[len(val) - 1] == '\n':
                    value.append(val[0:len(val) - 1]) # 去掉最后的换行符\n
                else:
                    value.append(val)

            res.append(value)
            i += 1
        return res

# res = getTxt('data.csv')
# print(res)