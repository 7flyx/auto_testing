# 基础语法部分
# 注意点：调用函数时，函数的定义必须在前面，跟C类似
import random


def hello():
    myName = input('请输入姓名') # input输入函数，里面可以写提示信息。input返回的默认是字符串
    print('hello world,'+ myName + '身高：'+ height + ' 体重：'+ weight)

def hello_twice():
    global height, weight # global 声明全局变量
    weight = input('体重：')
    height = input('身高：')

# 字符串的简单操作
def string_demo():
    word1 = 'hello world'
    word2 = word1.upper()
    word3 = word2.lower()
    line = '+' * 40 # 直接创建40个+号
    words = [word1, word2, word3] # 【】可以建列表，类似于数组
    print(line + words[random.randint(0, 2)] + line)



num1 = input('请输入一个数字:')
print('你输入的是数字%s'%num1,'可它的类型为：',type(num1)) #17、输出函数格式控制

string_demo()


# hello_twice()
# hello()
