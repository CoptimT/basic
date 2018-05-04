#-*- encoding: UTF-8 -*-
'''
@author: CoptimT
'''
from pykafka import KafkaClient
from pykafka.common import OffsetType
import datetime
from settings import KAFKA_HOST, KAFKA_TOPIC, KAFKA_GROUP,KAFKA_consumer_timeout_ms, KAFKA_PORT

class MyKafkaTools:
 
    def __init__(self):
        self.server = KAFKA_HOST+":"+KAFKA_PORT
        self.topic = KAFKA_TOPIC
        self.group = KAFKA_GROUP
        self.consumer_timeout_ms = KAFKA_consumer_timeout_ms
        self.consumer = None
        
    def beginConsumer(self):
        print(str(datetime.datetime.now()) + " start consumer ...")
        while True:
            message = self.consumer.consume()
            if message is not None:
                try:
                    print "message=====> "+message.value
                except (Exception) as e:
                    print(e)
        
    def simple_consumer(self, offset=0):
        client = KafkaClient(self.server)
        topic = client.topics[self.topic]
        partitions = topic.partitions
        last_offset = topic.latest_available_offsets()
        print("最近可用offset {}".format(last_offset))  # 查看所有分区
        self.consumer = topic.get_simple_consumer(self.group, partitions=[partitions[0]])  # 选择一个分区进行消费
        offset_list = self.consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset_list))  # 消费者拥有的分区offset的情况
#         self.consumer.reset_offsets([(partitions[0], offset)])  # 设置offset
#         offset_list = self.consumer.held_offsets
#         print("当前消费者分区offset情况{}".format(offset_list))  # 消费者拥有的分区offset的情况
        msg = self.consumer.consume()
        print("消费 :{}".format(msg.value.decode()))
        offset = self.consumer.held_offsets
        print("当前消费者分区offset情况{}".format(offset))
        self.consumer.commit_offsets()
        
    def balance_consumer(self, offset=0):
        client = KafkaClient(self.server)
        topic = client.topics[self.topic]
        # managed=True 设置后，使用新式reblance分区方法，不需要使用zk，而False是通过zk来实现reblance的
        self.consumer = topic.get_balanced_consumer(self.group, managed=True,
                                                    reset_offset_on_start=True,
                                                    auto_offset_reset=OffsetType.LATEST)
#         partitions = topic.partitions
#         print("分区 {}".format(partitions))
#         earliest_offsets = topic.earliest_available_offsets()
#         print("最早可用offset {}".format(earliest_offsets))
#         last_offsets = topic.latest_available_offsets()
#         print("最近可用offset {}".format(last_offsets))
#         offset = self.consumer.held_offsets
#         print("当前消费者分区offset情况{}".format(offset))
#         msg = self.consumer.consume()
#         offset = self.consumer.held_offsets
#         print("{}, 当前消费者分区offset情况{}".format(msg.value.decode(), offset))
#         self.consumer.commit_offsets()
        
if __name__ == '__main__':
    kt = MyKafkaTools()
    kt.balance_consumer()
#     kt.simple_consumer()
    kt.beginConsumer()