import json
import voyageai

# using our API key
vo = voyageai.Client()

with open("guinness_wine_dublin_cleaned.json", "r") as f:
    data = json.load(f)

# focusing on "reviews" field since that's what we are embedding
reviews_list = [place.get("reviews", "") for place in data.get("places", [])]

# getting embeddings for the reviews using "voyage-3-lite"
result = vo.embed(reviews_list, model="voyage-3-lite", input_type="document")

# new field to hold the embeddings
for place, embedding in zip(data.get("places", []), result.embeddings):
    place["embedding"] = embedding

# writing embeddings back to a new file
with open("embedded_guinness_wine_dublin_cleaned2.json", "w") as f:
    json.dump(data, f, indent=2)
