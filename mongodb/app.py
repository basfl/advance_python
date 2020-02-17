from pymongo import MongoClient
#from db_util import db_start, find_one, post_one, insert_many_records, find_value, delete_one, delete_all_except,update_one_record
from db_util.db_crud import *
from db_util import MongoDatabase

if __name__=="__main__":
    mongoDB=MongoDatabase()
    db = mongoDB.db_start()
    products=mongoDB.get_collection(db,'products')
    post1 = {"id": 0, "name": "post1", "time": datetime.datetime.now()}
    post2 = {"id": 0, "name": "post2", "time": datetime.datetime.now()}
    post3 = {"id": 0, "name": "post3", "time": datetime.datetime.now()}
    post4 = {"id": 0, "name": "post4", "time": datetime.datetime.now()}
    find_one(products)
    post_one(products,post1)
    insert_many_records(products, post2, post3, post4)
    find_value(products, "name", "post2")
    delete_one(products, "name", "post3")
    delete_all_except(products, "name", "post1")
    update_record(products, "name", "post1","name","post*1")


