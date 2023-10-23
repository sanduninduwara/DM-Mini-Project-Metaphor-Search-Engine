def match_query(connection, field, value,fuzzy=False):

    query = {
        "query": {
            "match": {
                field: value
            }
        }
    }
    
    if fuzzy:

        query = {
            "query": {
                "bool": {
                    "must": {
                        "match": {
                            field: {
                                "query": value,
                                "fuzziness": "AUTO"
                            }
                        }
                    }
                }
            }
        }
    
    resp = connection.search(index="poems", body=query)
    print("=======================", resp)
    return resp

