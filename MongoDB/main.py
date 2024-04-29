import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
collection = mydb['mycollection']
#insert one data
# dictionary = {'name':'Santosh','address':'dharan'}
# collection.insert_one(dictionary)

# dictionary = {'name':'Santosh','age': 24}
# collection.insert_one(dictionary)
#insert many data

insertdata = [
    {'_id':1,"name":"Suman","Location":"Ilam","age":23},
    {'_id':2,"name":"Sagar","Location":"Jhapa","age":22},
    {'_id':3,"name":"Monil","Location":"Dharan","age":25},
    {'_id':4,"name":"Rejina","Location":"Jhapa","age":24},
    {'_id':5,"name":"Susmita","Location":"Morang","age":23}
]
collection.insert_many(insertdata)