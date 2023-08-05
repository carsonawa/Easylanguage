import os
import time

#看啥看，这是备忘录
#Boolean（布尔值）

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
        os.system('cls')#没错，os库就用在这
    elif (s[0] == 'set'):#又是一大堆
        try:
            if (s[2] == '='):
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
            else:
                print('语法错误，意外的“', s[2], '”出现在代码中')
        except IndexError:
            print('索引错误，别只打单词')
    elif (s[0] == 'await'):#time.sleep(114514.1919810)（bushi）
        try:
            if (s[1] == 'int'):#文本：so？
                try:
                    s = int(s[2])
                    time.sleep(s)
                except:
                    print('语法错误，意外的“', s[2], '”出现在代码中')
            elif (s[1] == 'float'):
                try:
                    s = float(s[2])
                    time.sleep(s)
                except:
                    print('语法错误，意外的“', s[2], '”出现在代码中')
            elif (s[1] in blk):
                time.sleep(blk[s[1]])
            else:
                print('语法错误，意外的“', s[1], '”出现在代码中')
        except IndexError:
            print('索引错误，别只打单词')
    elif (s[0] == ''):
        pass
    else:
        print('语法错误,意外的“', s[0], '”出现在代码中')
    
print('语言版本0.5')#加载必要参数
print('需帮助输入“help”')
while True:#登登咚
    s = input('>>>')#获取输入
    if (s == 'run{'):
        while (s != '}'):
            s = input('...')
            jb.append(s)
        del jb[-1]
        for s in jb:
            ELfunction()
        for i in range(len(jb)):
            del jb[-1]
    elif (s == 'help'):#跑帮助
        print('')
        print('print (int/float/str) (text) :打印内容')
        print('set (text) = (int/float/str) (text) :创建/修改变量和值')
        print('await (int/float) (text)')
        print('run{script} :运行花括号里的脚本')
        print('* (text) :注释')
        print('clean :清空控制台文本')
        print('exit :退出程序')
        print('')
    elif (s == 'EL'):#awa
        print('语言版本0.4')
        print('需帮助输入“help”')
    elif (s == 'exit'):
        break
    elif (s != ''):#检测是不是空的，不加会报错
        ELfunction()#调用函数，开跑
        pass
#没了，就这样
