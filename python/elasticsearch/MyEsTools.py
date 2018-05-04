# -*- encoding: UTF-8 -*-

from elasticsearch import Elasticsearch  
from elasticsearch.helpers import bulk
from elasticsearch.helpers import streaming_bulk

class MyEsTools:
    def __init__(self,hosts,index,type):
        self.es = Elasticsearch(hosts=hosts.strip(',').split(','), timeout=5000)
        self.index = index
        self.type = type

    def bulk_data_v1(self,actions):
        success = bulk(self.es, actions, index=self.index, raise_on_error=True)
        print("bulk: "+str(success))
        
    def bulk_data(self,data):
        status = bulk(self.es, data, stats_only=True, raise_on_error=False, max_retries=5, initial_backoff=2, max_backoff=32)
        print("bulk: "+str(status))
        
    def streaming_bulk_data(self,data):
        streaming_bulk(self.es, data, index=self.index, raise_on_error=True)
        