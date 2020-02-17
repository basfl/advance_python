from pymongo import MongoClient


class CRUD:
    """
    find only one record
    from the collection
    """
    @staticmethod
    def find_one(collection_name):
        print(f'{collection_name.find_one()}')
    """
    post only one record
    to the collection
    """
    @staticmethod
    def post_one(collection_name, post):
        collection_name.insert_one(post)
    """
    insert many records
    to the collection
    """
    @staticmethod
    def insert_many_records(collection_name, *posts):
        posts_list = []
        print(posts)
        for post in posts:
            posts_list.append(dict(post))
            # collection_name.insert_one(post)
        expanded_list = [dict(i) for i in posts_list]
        # print(f"***********{l}")
        collection_name.insert_many(expanded_list)
    """
   find specific value 
   inside the collection docuemnt
   by passing key and value
    """
    @staticmethod
    def find_value(collection_name, key, value):
        try:
            result = collection_name.find_one({key: value})
            print(f"result is {result['name']}")
        except:
            print("Database Error Occoured")
    """
    delete only one specific record
    from collection
    """
    @staticmethod
    def delete_one(collection_name, key, value):
        collection_name.delete_one({key: value})
    """
     perform specific query and delete record
     base on the result of query
    """
    @staticmethod
    def delete_all_except(collection_name, key, value):
        query = {key: {"$ne": value}}
        # print(query)
        try:
            collection_name.delete_many(query)
        except:
            print("Database Error Occoured")
    """
    update value in collection and 
    add new value to the collection
    """
    @staticmethod
    def update_record(collection_name, key, value, update_key, update_value):
        myquery = {key: value}
        newvalues = {"$set": {update_key: update_value}}
        collection_name.update_many(myquery, newvalues)
        collection_name.update_many({update_key: update_value}, {
                                    "$set": {"updated": True}})
