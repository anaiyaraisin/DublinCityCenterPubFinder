from django.shortcuts import render
import os 
from dotenv import load_dotenv
from langchain_voyageai.embeddings import VoyageAIEmbeddings
from langchain_mongodb.vectorstores import MongoDBAtlasVectorSearch

load_dotenv()

def search_places(request):
    # get query from user 
    query = request.GET.get("query", "")
    results = []
    
    # same from our langchain_integration.py file
    if query:
        # use our API keys
        voyage_api_key = os.getenv("VOYAGE_API_KEY")
        connection_string = os.getenv("MONGO_URI")
        
        # this is our embeddings object. 
        embeddings = VoyageAIEmbeddings(
            voyage_api_key=voyage_api_key,
            model="voyage-3-lite"
        )
        
        # this is your database.collection
        namespace = "dublinfinder.placesinfo"
        
        # vector store with our embeddings model 
        vector_store = MongoDBAtlasVectorSearch.from_connection_string(
            connection_string=connection_string,
            namespace=namespace,
            embedding_key="embedding",
            index_name="vector_index",
            text_key="reviews",
            embedding=embeddings
        )

        # similarity search, LangChain handles embedding the query
        results_with_scores = vector_store.similarity_search_with_score(query, k=3)
        
        # post-process and make it look pretty
        processed_results = []
        maximum_char = 800

        for doc, score in results_with_scores:
            name = doc.metadata.get("displayName", {}).get("text", "Unknown")
            address = doc.metadata.get("formattedAddress", "Unknown")
            review_text = doc.page_content if doc.page_content else ""
            
            # refining it so we don't end in the middle of a sentence
            if len(review_text) > maximum_char:
                shortened = review_text[:maximum_char]
                last_period = shortened.rfind('.')
                if last_period != -1:
                    review = shortened[:last_period+1]
            
            processed_results.append({
                "name": name,
                "address": address,
                "review": review,
                "score": score
            })
        
        results = processed_results
    
    # template
    return render(request, "search_results.html", {"results": results, "query": query})
