import pymongo
from movie_recs import generate_embedding

# connect to the mongodb database
client = pymongo.MongoClient("MONGODB_CLIENT_LINK")
db = client.sample_mflix
collection = db.movies

hf_token = "YOUR_HF_TOKEN"
embedding_url = "HUGGING_FACE_URL"

# The search text I want to find similar movies
query = "imaginary characters from outer space at war"

# Generate the embeddings using the generate_embeddings function
results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hf",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
])

# Show the results
for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
