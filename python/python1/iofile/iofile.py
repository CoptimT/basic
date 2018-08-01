#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import os

def test1():
    msg = raw_input("请输入: ")
    print("你输入的内容是: ", msg)
def test2():
    # 写文件
    fo = open("foo.txt", "w")
    fo.write( "www.baidu.com!\nVery good site!\n")
    print "文件名: ", fo.name
    print "是否已关闭 : ", fo.closed
    print "访问模式 : ", fo.mode
    print "末尾是否强制加空格 : ", fo.softspace
    fo.close()
    print "是否已关闭 : ", fo.closed
def test3():
    # 读文件
    fr = open("foo.txt", "r+")
    msg = fr.read(20)
    print "读取的字符串是: ", msg
    msg = fr.readline()
    print "读取的字符串是: ", msg
    position = fr.tell()
    print "当前文件位置 : ", position
    position = fr.seek(0, 0)
    msg = fr.read(10)
    print "读取的字符串是: ", msg
    fr.close()
def test4():
    old = "foo.txt"
    new = "test.txt"
    os.rename(old, new)
    os.remove(new)
def test5():
    os.mkdir("test")
    print os.getcwd()
    os.chdir("test")
    print os.getcwd()
    os.chdir("..")
    os.rmdir("test")
def test6():
    try:
        f = open('foo.txt', 'r')
        print f.read()
    finally:
        if f:
            f.close()
    #但是每次都这么写实在太繁琐，所以，Python 引入了 with 语句来自动帮我们调用 close() 方法：
    with open('foo.txt', 'r') as f:
        print f.read()
    
if __name__ == "__main__":
    test6()

