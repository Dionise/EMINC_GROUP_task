from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import boto3
from bson import ObjectId

'''At the moment i will use primitive way to check if in the S3  exsiting json data was aded or delated 
Desrible is to use https://www.mongodb.com/developer/how-to/automated-continuous-data-copying-from-mongodb-to-s3/
'''


class Comunication:
    def __init__(self):
        self.service_name = ''
        self.region_name = ''
        self.aws_access_key_id = ''
        self.aws_secret_access_key =''

    def visualize_database():
            my_client = MongoClient("", server_api=ServerApi('1')) 
            dbname = my_client['sample_medicines']
            collection_name = dbname["medicinedetails"]
            return collection_name
    
    def triger(self):
     s3 = boto3.resource(
          service_name=self.service_name,
          region_name=self.region_name,
          aws_access_key_id = self.aws_access_key_id, 
          aws_secret_access_key = self.aws_secret_access_key
      )
     size = 0
     totalCount = 0
     for obj in s3.Bucket('datapatients').objects.all():
        print(obj)
        totalCount += 1
        size += obj.size    
        print('total size:')
        print("%.3f GB" % (size*1.0/1024/1024/1024))
        print('total count:')
        print(totalCount)
    
     toatlCount_mongodb = Comunication.visualize_database().count_documents({})
     
  

     

    def s3_to_mongo_db():
      s3 = boto3.resource(
        service_name=self.service_name,
        region_name=self.region_name,
        aws_access_key_id=self.aws_access_key_id,
        aws_secret_access_key= self.aws_secret_access_key
              )  
      for obj in s3.Bucket('datapatients').objects.all():
        file_content = obj.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        visualize_database().insert_many([json_content])



class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


'''
data = Comunication()
ok = data.triger()
'''



