# -*- coding: utf-8 -*-

__author__ = "Meritz"
__date__ = "creation: 2021-03-02, modification: 0000-00-00"

#################
#import
#################

import socket
from elasticsearch import Elasticsearch


doc = {
	  "SUBJECT": "입력테스트_3",
	  "URL": "URL입니다3.",
	  "CONTENT": "컨텐츠입니다3."
      }

def do_something_insert():
    index = "mkms_qna_v001"   

    es_client.index(index, doc_type="_doc", id="ID_20210306_03", body=doc)

def main():
    print("Hello Ela CRUD!")
    do_something_insert()

if __name__ == "__main__":
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    es_client = Elasticsearch(host=host_ip, port=9200)
    main()
