import pymongo
import requests

# connect to the client
client = pymongo.MongoClient("<YOUR_CLIENT_CONNECTION_LINK>")
db = client.sample_mflix
collection = db.movies

hf_token = "YOUR_HF_TOKEN"
embedding_url = "HUGGING_FACE_URL"

def generate_embedding(text: str) -> list[float]:
    """
        Generates embeddings for the given text and returns a JSON-like dictionary.

        Args:
            text (str): The input text for which embeddings are generated.
    """
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# replace each doc with a new doc containing the embedding
for doc in collection.find({'plot':{"$exists":True}}).limit(50):
    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
    collection.replace_one({'_id':doc['_id']}, doc)

