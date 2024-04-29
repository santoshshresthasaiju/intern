import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
collection = mydb['mycollection']
# dictionary = {'name':'Santosh','address':'dharan'}
# collection.insert_one(dictionary)

# dictionary = {'name':'Santosh','age': 24}
# collection.insert_one(dictionary)
insertdata = [
    {"name":"Suman","Location":"Ilam","age":23},
    {"name":"Sagar","Location":"Jhapa","age":22},
    {"name":"Monil","Location":"Dharan","age":25},
    {"name":"Rejina","Location":"Jhapa","age":24},
    {"name":"Susmita","Location":"Morang","age":23}
]
collection.insert_many(insertdata)