import json
import re

def extract_worker_id(worker):
    # Extract the worker's unique ID
    return worker.get('worker_id', None)

def extract_full_name(worker):
    # Extract full name of the worker (first name + last name)
    first_name = worker.get('first_name', '')
    last_name = worker.get('last_name', '')
    return f"{first_name} {last_name}"

def extract_email(worker):
    # Extract the worker's email
    return worker.get('email', None)

def extract_job_details(worker):
    # Extract job-related information like position, department, location, and supervisor
    job_details = worker.get('job_details', {})
    position = job_details.get('position', None)
    department = job_details.get('department', None)
    location = job_details.get('location', None)
    
    supervisor = job_details.get('supervisor', {})
    supervisor_id = supervisor.get('id', None)
    supervisor_name = supervisor.get('name', None)
    
    return {
        "position": position,
        "department": department,
        "location": location,
        "supervisor_id": supervisor_id,
        "supervisor_name": supervisor_name
    }

def extract_contact_details(worker):
    # Extract work and home contact information (phone and email)
    work_contact = worker.get('work_contact', {})
    home_contact = worker.get('home_contact', {})
    
    work_phone = work_contact.get('phone', None)
    work_email = work_contact.get('email', None)
    
    home_address = home_contact.get('address', None)
    home_phone = home_contact.get('phone', None)
    
    return {
        "work_phone": work_phone,
        "work_email": work_email,
        "home_address": home_address,
        "home_phone": home_phone
    }

def extract_custom_fields(worker):
    # Extract any custom fields that are added to the worker profile
    return worker.get('custom_fields', {})

def extract_employment_status(worker):
    # Extract the worker's employment status
    return worker.get('employment_status', None)

def extract_worker_details(worker):
    # Extract all worker-related metadata
    worker_id = extract_worker_id(worker)
    full_name = extract_full_name(worker)
    email = extract_email(worker)
    job_details = extract_job_details(worker)
    contact_details = extract_contact_details(worker)
    custom_fields = extract_custom_fields(worker)
    employment_status = extract_employment_status(worker)
    
    return {
        "worker_id": worker_id,
        "full_name": full_name,
        "email": email,
        "job_details": job_details,
        "contact_details": contact_details,
        "custom_fields": custom_fields,
        "employment_status": employment_status
    }

def extract_all_worker_details(workers_data):
    # Extract details for a list of workers
    worker_details = []
    for worker in workers_data:
        worker_details.append(extract_worker_details(worker))
    return worker_details

def extract_worker_name(worker):
    # Extract the worker's full name (first_name + last_name)
    return worker.get('first_name', '') + " " + worker.get('last_name', '')

def extract_worker_department(worker):
    # Extract the worker's department
    job_details = worker.get('job_details', {})
    return job_details.get('department', None)

def extract_worker_position(worker):
    # Extract the worker's position
    job_details = worker.get('job_details', {})
    return job_details.get('position', None)

def extract_worker_supervisor(worker):
    # Extract the supervisor's name and ID
    job_details = worker.get('job_details', {})
    supervisor = job_details.get('supervisor', {})
    return supervisor.get('name', None), supervisor.get('id', None)

def extract_worker_affiliation(worker):
    # Extract custom field ASU affiliation
    custom_fields = worker.get('custom_fields', {})
    return custom_fields.get('asu_affiliation', None)
