from pymongo import MongoClient
import datetime
import configparser
"""
reading values from
config file
"""
config = configparser.ConfigParser()
config.read('../mongodb/db.ini')


class MongoDatabase:
    """
    initializing mongodb using
    credentials provided in db.ini 
    property file

    """
    @staticmethod
    def db_start():
        print("**Connecting to Database**")
        user = config['mongodb']['user']
        password = config['mongodb']['pass']
        client = MongoClient(
            'mongodb+srv://'+user+':'+password+'@cluster0-x20zq.mongodb.net/test')
        db = client.ptest
        return db

    @staticmethod
    def get_collection(database, collection_name):
        return database.get_collection(collection_name)
