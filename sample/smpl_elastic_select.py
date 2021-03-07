# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################

import socket
from elasticsearch import Elasticsearch

index = "mkms_qna_v001"
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
es_client = Elasticsearch(host=host_ip, port=9200)

def do_something_select_all():
    body = {'size':1000, 'query':{ 'match_all':{}}}
    res = es_client.search(index=index, body=body)
    print(res)
    hits = res['hits']['hits']
    print("----------")
    print(hits)
    return res

def do_something_select_all_source():
    body = {
		    "size": 10000,
		    "_source": {
				"includes": [ "SUBJECT", "URL"],
   			},
			"query": {
			    "match_all": {}
			},
	}
    res = es_client.search(index=index, body=body)
    print(res)
    hits = res['hits']['hits']
    print("----------")
    print(hits)
    return res

def main():
    print("Hello Ela Search!")
    #do_something_select_all()
    do_something_select_all_source()

if __name__ == "__main__":
    main()
