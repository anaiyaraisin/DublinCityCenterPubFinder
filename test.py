import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_voyageai.embeddings import VoyageAIEmbeddings

load_dotenv()
voyage_api_key = os.getenv("VOYAGE_API_KEY")
connection_string = os.getenv("MONGO_URI")

embeddings = VoyageAIEmbeddings(
    voyage_api_key=voyage_api_key,
    model="voyage-3-lite"
)

query = (
    "Temple Bar. Outdoor seating. Guinness"
)
query_vector = embeddings.embed_query(query)

client = MongoClient(connection_string)
db = client["dublinfinder"]
collection = db["placesinfo"]

pipeline = [
    {
        "$vectorSearch": {
            "index": "vector_index",        
            "path": "embedding",            
            "queryVector": query_vector,   
            "numCandidates": 40,           
            "limit": 5,                     
            "similarity": "cosine"         
        }
    },
    {
        "$project": {
            "_id": 0,  
            "name": "$displayName.text",   
            "address": "$formattedAddress"
        }
    }
]


results = list(collection.aggregate(pipeline))

print("working?")
for doc in results:
    print(doc)
