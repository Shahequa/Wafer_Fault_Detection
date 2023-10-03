
from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# Uniform Resource Identifier
uri = "mongodb+srv://shahequa:shahequa@cluster0.elubqiy.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Create a database name and collection name
DATABASE_NAME = "shahequa"
COLLECTION_NAME = "waferfault"

# read the data as a dataframe
df = pd.read_csv("notebooks\data\wafer.csv")
df=df.drop("Unnamed: 0", axis=1)

# Convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

# Now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
