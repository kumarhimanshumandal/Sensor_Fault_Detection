# Here, whatever code I'll write will read the dataset and upload it to MongoDB

from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://himanshu:12345@cluster0.iegniez.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="datas"
COLLECTION_NAME='waferfault'

df = pd.read_csv(r"C:\Users\KIIT\Desktop\New folder\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

# Convert the data into list.
json_record=list(json.loads(df.T.to_json()).values())

"""JSON stands for JavaScript Object Notation.
It is a lightweight data format used to store and exchange data — easy for humans to read and write, and easy for machines to parse and generate.
"""
# Now this data into MongoDB
client [DATABASE_NAME] [COLLECTION_NAME].insert_many(json_record)