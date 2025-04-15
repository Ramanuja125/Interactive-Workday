from data_processing import get_bearer_token  
from indexing import index_and_store_worker_nodes  
from vectorstorage import run_semantic_search  
from LLM import run_model  

def data_chunk_and_save():
    print("Getting worker details and saving to worker_details.json file...")
    #get_bearer_token()  
    print("Saving to worker_details.json file complete\n")

    print("Indexing and storing worker details...")
    index_and_store_worker_nodes()  
    print("Indexing and storing complete")

def main():
    data_chunk_and_save() 
    while True:
        query = input("\nPlease enter a query related to workers (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Exiting the program.")
            break  # Exit the loop and end the program

        print("Running semantic search for worker details...")
        semantic_search, result_string = run_semantic_search(query)
        print(result_string)
        print("Semantic search complete\n")

        print("Running LLM model for worker details...")
        response = run_model(semantic_search, query)  
        print("LLM model finished\n")
        print("Response:", response)

if __name__ == "__main__":
    main()
