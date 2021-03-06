# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################
import socket
from elasticsearch import Elasticsearch

document = {
    "settings": {
        "number_of_shards": 6,
        "number_of_replicas": 2
    },
    "mappings":{
        "properties": {
            "ID": {
                "type": "keyword"
            },
            "SUBJECT": {
                "type": "text"
            },
            "URL": {
                "type": "keyword"
            },
            "CONTENT": {
                "type": "text"
            }
        }
    }
}

def do_something():
    if es.indices.exists(index='mkms_qna_v001'):
        print("Already existed index")
        es.indices.delete(index='mkms_qna_v001', ignore=[400, 404])
        # es.indices.create(index='stt', body=document)
    else:
        es.indices.create(index='mkms_qna_v001', body=document)
        # Max result window update
        es.indices.put_settings(index='mkms_qna_v001', body={"index": {"max_result_window": 50000}})
        # Max inner result window update
        es.indices.put_settings(index='mkms_qna_v001', body={"index": {"max_inner_result_window": 50000}})
        # Refresh
        es.indices.refresh(index='mkms_qna_v001')

def main():
    print("Hello Elastic!")
    do_something()

if __name__ == "__main__":
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    es = Elasticsearch(host=host_ip, port=9200)

    main()
