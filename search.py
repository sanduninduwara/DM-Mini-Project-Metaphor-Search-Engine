# from datetime import datetime
# from elasticsearch import Elasticsearch
# es = Elasticsearch([{'host': 'localhost', 'port': 9200, "scheme": "http"}])


# resp = es.get(index="poems",id="CE6OUYsBcJOyq73a64aL")
# print(resp)

# def get_poem(connection,id):
#     resp = connection.get(index="poems",id=id)
#     return resp

def match_query(connection,field, value):
    query = {
        "query": {
            "match": {
                field: value
            }
        }
    }
    resp = connection.search(index="poems", body=query)
    print("=======================",resp)
    return resp