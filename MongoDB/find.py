import pymongo

if  __name__ == "__main__":
    print("welcome to MongoDB")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print(myclient)
    mydb = myclient['mydatabase']
    collection = mydb['mycollection']

    data = collection.find({'name':'Santosh'})
    for item in data:
        print(item)
        
