import requests
import json

# Workday API endpoints (replace with actual URLs)
LOGIN_URL = "https://workday-api.com/login"
WORKERS_URL = "https://workday-api.com/workers"

# can be written to be sent as a parameter as well 
USERNAME = "rkrish79@asu.edu"
PASSWORD = "Workday@123"

def get_bearer_token():
    """Logs in and retrieves the bearer token."""
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    
    response = requests.post(LOGIN_URL, json=payload)
    
    if response.status_code == 200:
        fetch_worker_details(response.json().get("access_token"))
        return response.json().get("access_token")  
        
    else:
        print(f"Failed to log in: {response.text}")
        return None

def fetch_worker_details(token):
    """Fetches worker details using the bearer token."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    response = requests.get(WORKERS_URL, headers=headers)
    
    if response.status_code == 200:
        save_worker_details(response.json())
        return response.json()
    else:
        print(f"Failed to fetch worker details: {response.text}")
        return None

def save_worker_details(data, filename="worker_details.json"):
    """Saves the worker details to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print(f"Worker details saved to {filename}")

def main():
    """Main function to execute the API calls and save data."""
    get_bearer_token()

if __name__ == "__main__":
    main()
