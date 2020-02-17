import datetime
from pymongo import MongoClient
#from db_util import db_start, find_one, post_one, insert_many_records, find_value, delete_one, delete_all_except,update_one_record
from db_util import CRUD
from db_util import MongoDatabase

"""
collection documents 
to be used for app.py
"""
post1 = {"id": 0, "name": "post1", "time": datetime.datetime.now()}
post2 = {"id": 1, "name": "post2", "time": datetime.datetime.now()}
post3 = {"id": 2, "name": "post3", "time": datetime.datetime.now()}
post4 = {"id": 3, "name": "post4", "time": datetime.datetime.now()}

if __name__ == "__main__":
    mongoDB = MongoDatabase()
    db = mongoDB.db_start()
    products = mongoDB.get_collection(db, 'products')
    crud = CRUD()
    crud.find_one(products)
    crud.post_one(products, post1)
    crud.insert_many_records(products, post2, post3, post4)
    crud.find_value(products, "name", "post2")
    crud.delete_one(products, "name", "post3")
    crud.delete_all_except(products, "name", "post1")
    crud.update_record(products, "name", "post1", "name", "post*#1")
