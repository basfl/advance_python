from pymongo import MongoClient
import datetime
import configparser
"""
reading values from
config file
"""
config = configparser.ConfigParser()
config.read('../mongodb/db.ini')


def db_start():
    print("**Connecting to Database**")
    user = config['mysql']['user']
    password = config['mysql']['pass']
    client = MongoClient(
        'mongodb+srv://'+user+':'+password+'@cluster0-x20zq.mongodb.net/test')
    db = client.ptest
    return db


def find_one(collection_name):
    print(f'{collection_name.find_one()}')


def post_one(collection_name, post):
    collection_name.insert_one(post)


def insert_many_records(collection_name, *posts):
    posts_list = []
    print(posts)
    for post in posts:
        posts_list.append(dict(post))
        # collection_name.insert_one(post)
    expanded_list = [dict(i) for i in posts_list]
    #print(f"***********{l}")
    collection_name.insert_many(expanded_list)


def find_value(collection_name, key, value):
    try:
        result = collection_name.find_one({key: value})
        print(f"result is {result['name']}")
    except:
        print("Database Error Occoured")


def delete_one(collection_name, key, value):
    collection_name.delete_one({key: value})


def delete_all_except(collection_name, key, value):
    query = {key: {"$ne": value}}
    #print(query)
    try:
        collection_name.delete_many(query)
    except:
        print("Database Error Occoured")

def update_record(collection_name,key,value,update_key,update_value):
    myquery = { key: value }
    newvalues = { "$set": { update_key: update_value } }
    collection_name.update_many(myquery, newvalues)
    collection_name.update_many({ update_key: update_value }, { "$set": { "updated": True } })
   

