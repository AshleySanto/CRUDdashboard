from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47655/?authMechanism=DEFAULT&authSource=AAC' %(username, password))
        self.database = self.client['AAC']

    #Creates new document 
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    #Read multiple documents
    def read_all(self,data):
        cursor = self.database.animals.find(data,{"_id":False})
        return cursor
        
    #Read a specified document
    def read(self,data):
        return self.database.animals.find_one(data)
    
    #Update document within the database
    def update(self,original,new):
        if new is not None:
            updateResult = self.database.animals.update_many(original,new)
            #Print number of updated documents
            result = "Documents updated: " + json.dumps(updateResult.modified_count)
            return result
        else:
            raise Exception("Document not found in database")

    #Delete document within database
    def delete(self, data):
        if data is not None:
            deleteResult = self.database.animals.delete_many(data)
            #print number of deleted documents
            result = "Documents deleted: " + json.dumps(deleteResult.count)
            return result
        else:
            raise Exception("No documents found to delete")
        