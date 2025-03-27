import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# get the environment variable and connect 
connection_string = os.getenv("MONGO_URI")
connect = MongoClient(connection_string)

# specify our database and collection
database = connect["dublinfinder"]
collection = database["placesinfo"]

# load in our json file
with open("embedded_guinness_wine_dublin_cleaned2.json", "r") as file:
    data = json.load(file)

# our json file starts with "places" so this is just making sure it fits
if isinstance(data,dict) and "places" in data:
    places = data["places"]

# use insert_many since we have 40 docs
result = collection.insert_many(places)



