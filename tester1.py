# Download all the 3 python files and the tester.sh files and run the shell script by - ./tester.sh
# LLM and codeChunksHelper
# tests LLM And gets sample response for the query statment
# tests code chunks helper and gives function name

def test_llm():
    try:
        from LLM import run_model
        print("------------------------------------------------------------------------")
        print("Testing LLM...")

        # Sample worker data used as context
        worker_context = """
        Kevin Gilmore is an Insurance claims handler in the Leverage B2C Interfaces department.
        He works at the Polytechnic location. His supervisor is Heather King (ID: 14941).
        Kevin's email is kevin.gilmore28@asu.edu. His worker ID is W10728.
        """

        # The question to ask the model
        question = "Who is the supervisor of Kevin Gilmore?"

        response = run_model(worker_context, question)
        
        if response and "Heather King" in response:
            print(f"Pass - LLM ran successfully, response: {response.strip()}")
        else:
            print(f"Fail - LLM did not return expected answer. Response: {response.strip()}")
        
        print("------------------------------------------------------------------------")
    except Exception as e:
        print(f"Fail - LLM: {e}")
        print("------------------------------------------------------------------------")
def test_code_chunks_helper():
    try:
        from codechunksHelper import extract_worker_details
        
        print("------------------------------------------------------------------------")
        print("Testing codeChunksHelper...")

        # Load the sample JSON worker data (as shown in your message)
        sample_worker_json = {
            "id": 14284,
            "worker_id": "W10728",
            "first_name": "Kevin",
            "last_name": "Gilmore",
            "email": "kevin.gilmore28@asu.edu",
            "job_details": {
                "position": "Insurance claims handler",
                "department": "Leverage B2C Interfaces",
                "location": "Polytechnic",
                "supervisor": {
                    "id": 14941,
                    "name": "Heather King"
                }
            },
            "employment_status": "Active",
            "hire_date": "2024-03-30",
            "worker_type": "Employee",
            "work_contact": {
                "phone": "+1-201-534-6525",
                "email": "kevin.gilmore28@asu.edu"
            },
            "home_contact": {
                "address": "0686 Justin Island, Jamestown, WY 40622",
                "phone": "001-860-658-3330x8713"
            },
            "custom_fields": {
                "asu_affiliation": "Staff",
                "campus_id": "A6918812"
            }
        }

        # Call the function with proper structure
        result = extract_worker_details(sample_worker_json)

        # Test expected output
        assert result['worker_id'] == "W10728"
        assert result['full_name'] == "Kevin Gilmore"
        assert result['email'] == "kevin.gilmore28@asu.edu"
        assert result['job_details']['supervisor_name'] == "Heather King"
        assert result['employment_status'] == "Active"
        assert result['custom_fields']['asu_affiliation'] == "Staff"

        print("Pass - Worker details extracted correctly.")
        print("------------------------------------------------------------------------")
    
    except AssertionError:
        print("Fail - Output mismatch in extracted worker details.")
        print("------------------------------------------------------------------------")
    except Exception as e:
        print(f"Fail - codeChunksHelper: {e}")
        print("------------------------------------------------------------------------")


if __name__ == "__main__":
    test_llm()
    test_code_chunks_helper()
