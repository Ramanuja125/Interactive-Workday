import faiss
from sentence_transformers import SentenceTransformer
import json

class WorkerVectorStorage:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        # Load pre-trained model for worker embeddings
        self.model = SentenceTransformer(model_name)

        # Dimension of embeddings from the model
        self.dim = self.model.get_sentence_embedding_dimension()

        # Create Faiss index (L2 distance)
        self.index = faiss.IndexFlatL2(self.dim)

        # Store original worker details for reference
        self.worker_details = []

    def add_worker_details(self, workers):
        # Generate embeddings for the workers' details (e.g., first_name, last_name, position, and department)
        worker_details = [
            f"{worker['first_name']} {worker['last_name']} - {worker['job_details']['position']} in {worker['job_details']['department']}"
            for worker in workers
        ]

        # Generate embeddings
        embeddings = self.model.encode(worker_details, convert_to_tensor=False).astype('float32')

        # Add embeddings to Faiss index
        self.index.add(embeddings)

        # Store full worker details
        self.worker_details.extend(workers)

    def search_worker_details(self, query, top_k=3):
        query_embedding = self.model.encode([query], convert_to_tensor=False).astype('float32')

        distances, indices = self.index.search(query_embedding, top_k * 2)  # Search more to allow for duplicates

        results = []
        seen_ids = set()
        for dist, idx in zip(distances[0], indices[0]):
            similar_worker = self.worker_details[idx]

            # Skip if we've already seen this worker's ID
            if similar_worker['id'] in seen_ids:
                continue

            similarity = 1 / (1 + dist)
            results.append((similar_worker, similarity))
            seen_ids.add(similar_worker['id'])

            if len(results) == top_k:
                break

        return results

def load_workers_from_json(file_path):
    """Load worker details from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)

    workers = []

    if isinstance(data, list):
        # Handle multiple worker entries
        for entry in data:
            if isinstance(entry, dict) and "worker" in entry:
                worker = entry["worker"]
                workers.append({
                    "id": worker["id"],
                    "worker_id": worker["worker_id"],
                    "first_name": worker["first_name"],
                    "last_name": worker["last_name"],
                    "email": worker["email"],
                    "job_details": worker["job_details"],
                    "employment_status": worker["employment_status"],
                    "hire_date": worker["hire_date"],
                    "worker_type": worker["worker_type"],
                    "work_contact": worker["work_contact"],
                    "home_contact": worker["home_contact"],
                    "custom_fields": worker["custom_fields"]
                })
    elif isinstance(data, dict) and "worker" in data:
        # Handle single worker case (in case JSON is not wrapped in a list)
        worker = data["worker"]
        workers.append({
            "id": worker["id"],
            "worker_id": worker["worker_id"],
            "first_name": worker["first_name"],
            "last_name": worker["last_name"],
            "email": worker["email"],
            "job_details": worker["job_details"],
            "employment_status": worker["employment_status"],
            "hire_date": worker["hire_date"],
            "worker_type": worker["worker_type"],
            "work_contact": worker["work_contact"],
            "home_contact": worker["home_contact"],
            "custom_fields": worker["custom_fields"]
        })

    print(f"Total number of workers stored: {len(workers)}")  # Debugging line
    return workers


def run_semantic_search(query):
    worker_search = WorkerVectorStorage()

    # Load worker details from a JSON file
    file_path = "worker_details.json"  # Path to your JSON file
    worker_details = load_workers_from_json(file_path)

    # Add worker details to the index
    worker_search.add_worker_details(worker_details)

    # Perform the semantic search
    results = worker_search.search_worker_details(query)

    # Get the results as a string
    results_string = "Similar workers:\n"
    for worker, similarity in results:
        results_string += f"ID: {worker['id']}\n"
        
        # Constructing a worker details string
        worker_details_str = f"{worker['first_name']} {worker['last_name']} - {worker['job_details']['position']} in {worker['job_details']['department']}"
        
        results_string += f"Details:\n{worker_details_str}\n"
        results_string += f"Similarity Score: {similarity:.4f}\n"
        results_string += "--------------------------------------------------------------------\n"

    return results, results_string

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="The query to run semantic search on")

    args = parser.parse_args()
    run_semantic_search(args.query)
