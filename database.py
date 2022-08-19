import pymongo

passd = "ckZpYU8HGpnc5i9i"
named = "CopySys"

client = pymongo.MongoClient("mongodb+srv://test:"+passd+"@cluster1.9glic.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database(named)

class user():
    def findsession(collection, Owenr):
        collection = db[collection]
        session = {"Owenr":Owenr}
        data = collection.find(session)
        countsessions = collection.count_documents(session)
        return data, countsessions

    def addsession(collection, Owenr, Session):
        collection = db[collection]
        newsession = {"Owenr":Owenr, "Session":Session}
        collection.insert_one(newsession)
    
    def editsession(collection, Owenr, Session):
        collection = db[collection]
        session = {"Owenr":Owenr}
        new = {"$set":{"Session":Session}}
        collection.update_one(session, new)

    def addchannel(collection, Owenr, target, name, share, formatS):
            collection = db[collection]
            newschannel = {"Owenr":Owenr, "target":target, "name":name, "share":share, "formatS":formatS}
            collection.insert_one(newschannel)

    def updatechannel1(collection, Owenr, formatS, name):
        collection = db[collection]
        formatS1 = {"Owenr":Owenr, "name":name}
        new = {"$set":{"formatS":formatS}}
        collection.update_one(formatS1, new)

    def updatechannel2(collection, Owenr, target, name, name1):
        collection = db[collection]
        channel = {"Owenr":Owenr, "name":name1}
        new = {"$set":{"target":target, "name":name}}
        collection.update_one(channel, new)

    def updatechannel3(collection, Owenr, share, name1):
        collection = db[collection]
        channel = {"Owenr":Owenr, "name":name1}
        new = {"$set":{"share":share}}
        collection.update_one(channel, new)

    def deletechannel(collection, Owenr, name1):
        collection = db[collection]
        channel = {"Owenr":Owenr, "name":name1}
        collection.delete_one(channel)