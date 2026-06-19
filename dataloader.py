import json

def load_candidates(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def load_job_description():
    return "Your job description text here."
