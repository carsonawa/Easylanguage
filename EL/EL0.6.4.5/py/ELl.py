from os import system
from time import sleep

#看啥看，这是备忘录
#Boolean（布尔值）

w = 'hello'
nc = 0
yxk = []
nc = {}
blk = {}
jb = []
s = 'str'

def ELfunction():
    global blk
    global s
    s = s.split()
    if (s[0] == 'print'):#print int hello_world 花言鸟语（doge）
        try:
            if (s[1] == 'int'):#整数类别
                try:
                    s = int(s[2])
                    print(s)
                except:
                    print('类型错误，请检查内容（转整数）')
            elif (s[1] == 'float'):#小数类别
                try:
                    s = float(s[2])
                    print(s)
                except:
                    print('类型错误，请检查内容（转浮点数）')
            elif (s[1] == 'str'):#文本类别
                try:
                    s = str(s[2])
                    s = s.split('_')
                    s = ' '.join(s)
                    print(s)
                except:
                    print('类型错误，请检查内容（转字符串）')
            elif (s[1] in blk):#打印变量
                print(blk[s[1]])
            else:
                print('语法错误，意外的“', s[1], '”出现在代码中')
        except IndexError:#只输入“print”的结果
            print('索引错误，别只打单词')
    elif (s[0] == '*'):#一下为杂乱小脚本，没啥可讲
        pass
    elif (s[0] == 'clean'):
        system('cls')#没错，os库就用在这
    elif (s[0] == 'var'):#又是一大堆,搞变量
        try:
            if (s[2] == '='):
                try:
                    nc['1'] = s[3]
                    if (nc['1'] == 'int'):
                        try:
                            blk[s[1]] = int(s[4])
                        except:
                            print('类型错误，请检查内容（转整数）')
                    elif (nc['1'] == 'float'):
                        try:
                            blk[s[1]] = float(s[4])
                        except:
                            print('类型错误，请检查内容（转浮点数）')
                    elif (nc['1'] == 'str'):
                        try:
                            nc['2'] = s[1]
                            s = str(s[4])
                            s = s.split('_')
                            blk[nc['2']] = ' '.join(s)
                        except:
                            print('类型错误，请检查内容（转字符串）')
                    elif (nc[nc['1']] in blk):
                        blk[s[1]] = 1
                    else:
                        print('语法错误，意外的“', s[3], '”出现在代码中')
                except:
                    print('索引错误，别只打单词')
            else:
                print('语法错误，意外的“', s[2], '”出现在代码中')
        except IndexError:
            blk[s[1]] = 0
    elif (s[0] in blk):
        try:
            if (s[1] == '='):#设置值
                try:
                    if (s[2] == 'int'):
                        try:
                            blk[s[0]] = int(s[3])
                        except:
                            print('类型错误，请检查内容（转整数）')
                    elif (s[2] == 'float'):
                        try:
                            blk[s[0]] = float(s[3])
                        except:
                            print('类型错误，请检查内容（转字符串）')
                    elif (s[2] == 'str'):
                        blk[s[0]] = s[3]
                    else:
                        print('语法错误，意外的“', s[2], '”出现在代码中')
                except:
                    print('索引错误，别只打单词')
            elif(s[1] == '+='):
                try:
                    if (s[2] == 'int'):
                        try:
                            blk[s[0]] += int(s[3])
                        except:
                            print('类型错误，请检查内容（转整数）')
                    elif (s[2] == 'float'):
                        try:
                            blk[s[0]] += float(s[3])
                        except:
                            print('类型错误，请检查内容（转字符串）')
                    else:
                        print('语法错误，意外的“', s[2], '”出现在代码中')
                except:
                    print('索引错误，别只打单词')
            elif(s[1] == '-='):
                try:
                    if (s[2] == 'int'):
                        try:
                            blk[s[0]] -= int(s[3])
                        except:
                            print('类型错误，请检查内容（转整数）')
                    elif (s[2] == 'float'):
                        try:
                            blk[s[0]] -= float(s[3])
                        except:
                            print('类型错误，请检查内容（转字符串）')
                    else:
                        print('语法错误，意外的“', s[2], '”出现在代码中')
                except:
                    print('索引错误，别只打单词')
        except IndexError:
            print(blk[s[0]])
    elif (s[0] == 'await'):#sleep(114514.1919810)（bushi）
        try:
            if (s[1] == 'int'):#文本：so？
                try:
                    s = int(s[2])
                    sleep(s)
                except:
                    print('语法错误，意外的“', s[2], '”出现在代码中')
            elif (s[1] == 'float'):
                try:
                    s = float(s[2])
                    sleep(s)
                except:
                    print('语法错误，意外的“', s[2], '”出现在代码中')
            elif (s[1] in blk):
                try:
                    sleep(blk[s[1]])
                except:
                    print('类型错误，不是整数或浮点数')
            else:
                print('语法错误，意外的“', s[1], '”出现在代码中')
        except IndexError:
            print('索引错误，别只打单词')
        except IndexError:
            print('索引错误，别只打单词')
    elif (s[0] == ''):
        pass
    else:
        print('语法错误,意外的“', s[0], '”出现在代码中')

while True:
    s = input('>>')
    f = open(s, 'r', encoding="utf-8")
    line = f.readline()
    while (line != ""):
        s = line
        ELfunction()
        line = f.readline
    input('按回车继续……')