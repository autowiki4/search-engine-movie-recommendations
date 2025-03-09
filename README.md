# 🎬 Advanced Search Engine - Movie Recommendation System 🚀

In my CSCI-110 class, we explored search algorithms for building a search engine. However, the search feature often produced inaccurate results — similar to how LinkedIn's search sometimes delivers unrelated matches when a query is slightly off.

This made me curious: Why does Google still deliver relevant results even with typos or vague queries? The key difference lies in **Vector Search** — a technique that represents text as numerical vectors to find semantic similarities instead of exact keyword matches. Inspired by this, I built a **movie recommendation system** that suggests movies based on plot relevance.

## 🔍 How It Works  
1. **Embedding Generation**: Movie plot descriptions are converted into numerical vectors using the `all-MiniLM-L6-v2` sentence transformer from Hugging Face.  
2. **Similarity Comparison**: The search query is also transformed into a vector.  
3. **Recommendation Process**: The **dot product** is used to measure the similarity between the query vector and movie plot vectors. Movies with higher similarity scores are recommended.  

This approach helps the system recommend movies with similar meanings, even if the search terms don't exactly match the plot descriptions.

## 🛠️ Technologies Used  
- **MongoDB Atlas** → Stores movie data and supports vector-based searches.  
- **Hugging Face** → Provides the sentence transformer model for generating text embeddings.  
- **PyCharm** → My IDE for writing and testing the code although you cna use any Python IDE  

## 📚 Python Libraries  
To install the necessary libraries, run:  

```sh
pip install pymongo requests
```
 
- `pymongo` → For connecting and interacting with MongoDB.  
- `requests` → For making API calls to Hugging Face.  

## ⚠️ Limitations  
- The system currently embeds only the first **50 movies** due to resource constraints.  
- Full dataset embeddings (**20k+ movies**) would require more computational resources or access to paid APIs.  
- Precomputed embeddings from other APIs (like OpenAI) couldn't be reused because vector embeddings are model-specific.  

## 🙏 Acknowledgments 
- This project was inspired by [freeCodeCamp YouTUbe tutorial](https://youtu.be/JEBDfGqrAUA?si=jeDYGXICExUsDtQf)  

