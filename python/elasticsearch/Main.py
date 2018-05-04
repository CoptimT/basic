# -*- encoding: UTF-8 -*-
from pypinyin import pinyin,lazy_pinyin
import MyEsTools as es

class Main:
    def __init__(self):
        pass
    
if __name__ == '__main__':
    tool = es.MyEsTools('10.116.27.131','test','cn')
    ACTIONS = []
    source = {
        "data": "test"  
    }
    action = {
        "_index": tool.index,  
        "_type": tool.type,  
        "_source": source,
        "_id":"车质网_12345"
    }
    ACTIONS.append(action)
#     tool.bulk_data(ACTIONS)
#     print pinyin(unicode("车质网","UTF-8"))
    print pinyin("车质网".decode("utf-8"),errors='ignore')
    print ''.join(lazy_pinyin("太平洋汽车网".decode("utf-8"),errors='ignore'))
    print ''.join(lazy_pinyin("车质网%".decode("utf-8")))


