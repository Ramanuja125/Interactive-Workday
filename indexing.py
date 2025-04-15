from rocksdict import Rdict, Options
import json
import uuid

class WorkerIndexer:
    def __init__(self, db_path):
        # Initialize the RocksDB options and database
        opt = Options()
        opt.create_if_missing(True)
        self.db = Rdict(db_path, options=opt)

    def store_worker(self, worker):
        worker_id = worker['worker_id']
        worker_email = worker['email']

        # Check if worker with the same email already exists
        if f"email:{worker_email}" in self.db:
            #print(f"Duplicate worker found with email {worker_email}, skipping storage.")
            return  # Skip storing if it's a duplicate

        # Store the full worker record
        self.db[f"worker:{worker_id}"] = json.dumps(worker)

        # Index by worker attributes
        self.db[f"email:{worker_email}"] = worker_id
        self.db[f"position:{worker['job_details']['position']}"] = worker_id
        self.db[f"department:{worker['job_details']['department']}"] = worker_id
        self.db[f"location:{worker['job_details']['location']}"] = worker_id
        self.db[f"worker_type:{worker['worker_type']}"] = worker_id
        self.db[f"status:{worker['employment_status']}"] = worker_id

    def count_workers(self):
        # Count total number of workers stored
        worker_count = 0
        for db_key in self.db.keys():
            if db_key.startswith("worker:"):
                worker_count += 1
        return worker_count

    def close(self):
        # Close the RocksDB connection
        self.db.close()

def generate_worker_id():
    return str(uuid.uuid4())

def load_workers_from_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def index_and_store_worker_nodes():
    # Initialize the worker indexer with RocksDB file path
    indexer = WorkerIndexer("worker_nodes.db")

    # Load workers data from the JSON file
    workers = load_workers_from_json("worker_details.json")

    # Iterate over the list of workers
    for worker_entry in workers:  # Each entry is a dictionary
        worker = worker_entry.get("worker", {})  # Extract worker data
        if worker:
            worker["worker_id"] = generate_worker_id()  # Generate unique ID
            indexer.store_worker(worker)
    
    # Get the total number of workers stored
    total_workers = indexer.count_workers()
    print(f"Total number of workers stored: {total_workers}")

    # Close the database
    indexer.close()

if __name__ == "__main__":
    index_and_store_worker_nodes()
