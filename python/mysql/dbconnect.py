# -*- coding: UTF-8 -*-
'''
Created on 2018-5-4

@author: CoptimT
'''
import pymysql
import tools
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MyClass(object):

    def __init__(self, params):
        print("-----------华丽分割线------------")
        
if __name__ == '__main__':
    print("-----------华丽分割线1------------")
    try:
        # 连接MySQL数据库
        connection = pymysql.connect(host='172.17.170.176', port=3306, user='root', password='', db='', 
                                     charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        # 通过cursor创建游标
        cursor = connection.cursor()
        # 执行数据查询
        sql = "SELECT `series`, `brand` FROM `meta_series`"
        cursor.execute(sql)
        #查询数据库单条数据
#         result = cursor.fetchone()
#         tools.UniPrinter().pprint(result)
        
        print("-----------华丽分割线------------")
        brands={}
        #查询数据库多条数据
        result = cursor.fetchall()
        for data in result:
            print(data)
            brands[data["series"]]=data["brand"]
            break
        print(str(brands))
        
    except (Exception) as e:
        print(e)
    finally:
        # 关闭数据连接
        connection.close()
        print("-----------华丽分割线2------------")
    
    
    
    