from pymongo import MongoClient
#from db_util import db_start, find_one, post_one, insert_many_records, find_value, delete_one, delete_all_except,update_one_record
from db_util.db_crud import *
db = db_start()
products = db.get_collection('products')
find_one(products)
post1 = {"id": 0, "name": "post1", "time": datetime.datetime.now()}
post2 = {"id": 0, "name": "post2", "time": datetime.datetime.now()}
post3 = {"id": 0, "name": "post3", "time": datetime.datetime.now()}
insert_many_records(products, post1, post2, post3)
find_value(products, "name", "post2")
delete_one(products, "name", "post3")
delete_all_except(products, "name", "post1")
update_record(products, "name", "post1","name","post*1")

