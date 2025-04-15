# Download all the 3 python files and the tester.sh files and run the shell script by - ./tester.sh
# code rag
# tests code RAG
# Tests data_chunk_and_save and prints chunk distribution by individual repos

import os
import json

def test_RAG():
    try:
        from RAG import data_chunk_and_save
        print("------------------------------------------------------------------------")
        print("Testing CodeRAG...")

        # Suppress unwanted output
        import os
        with open(os.devnull, 'w') as fnull:
            original_stdout = os.dup(1)
            original_stderr = os.dup(2)
            os.dup2(fnull.fileno(), 1)
            os.dup2(fnull.fileno(), 2)

            try:
                data_chunk_and_save()
            finally:
                os.dup2(original_stdout, 1)
                os.dup2(original_stderr, 2)

        # Load the worker data
        with open("worker_details.json", "r") as file:
            workers = json.load(file)

        if not workers or not isinstance(workers, list):
            print("Fail - worker_details.json is empty or improperly formatted.")
            return

        # Print meaningful worker distribution, e.g., by department
        department_distribution = {}
        for worker in workers:
            dept = worker.get("job_details", {}).get("department", "Unknown")
            department_distribution[dept] = department_distribution.get(dept, 0) + 1

        print("Pass - CodeRAG processed and saved worker details.")
        print("------------------------------------------------------------------------")
        # print("Worker Distribution by Department:")
        # for dept, count in sorted(department_distribution.items(), key=lambda x: x[1], reverse=True):
            # print(f"{dept}: {count} workers")
        # print("------------------------------------------------------------------------")

    except Exception as e:
        print(f"Fail - CodeRAG: {e}")

if __name__ == "__main__":
    test_RAG()
