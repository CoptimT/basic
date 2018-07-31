#!/bin/env python
# -*- coding: UTF-8 -*-

import argparse

def test1():
    parser = argparse.ArgumentParser()
    parser.add_argument('echo')
    args = parser.parse_args()
    print(args)
    print(args.echo)
    # > python test.py ofo
    # Namespace(echo='ofo')
    # ofo
def test2():
    parser = argparse.ArgumentParser(description = 'this is a description')
    parser.add_argument('--ver', '-v', action = 'store_true', help = 'hahaha')
    # 将变量以标签-值的字典形式存入args字典
    args = parser.parse_args()
    print(args)
    if args.ver:
        print("Ture")
    else:
        print("False")
    # > python test.py -v
    # > python test.py --ver
    # Namespace(ver=True)
    # Ture

    # > python test.py -h
    # usage: test.py [-h] [--ver]
    # this is a description
    # optional arguments:
    #   -h, --help  show this help message and exit
    #   --ver, -v   hahaha
def test3():
    parser = argparse.ArgumentParser(description = 'this is a description')
    parser.add_argument('--ver', '-v', required = True, type = int)
    args = parser.parse_args()
    print(args)
    if args.ver:
        print("Ture")
    else:
        print("False")
    # > python test.py -v
    # usage: test.py [-h] --ver VER
    # test.py: error: argument --ver/-v: expected one argument

    # > python test.py --ver 10
    # Namespace(ver=10)
    # Ture
    
    
    
    
if __name__ == "__main__":
    test3()


