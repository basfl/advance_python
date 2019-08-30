from pymongo import MongoClient
# client = MongoClient()
client = MongoClient(
    'mongodb+srv://baslf:qazwsx123@cluster0-svlvn.mongodb.net/test?retryWrites=true&w=majority')
# client = pymongo.MongoClient("mongodb+srv://baslf:qazwsx123@cluster0-svlvn.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
products = db.get_collection('products')
print(f'{products.find_one()}')
