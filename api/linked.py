import requests

def get_job_postings():
    url = "https://api.linkedin.com/v2/jobs/search"
    params = {
        "q": "software engineer",
        "location": "San Francisco",
    }
    headers = {
        "Authorization": "Bearer TOKEN",
    }
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["jobs"]
    else:
        return None

def show_job_postings(job_postings):
    for job_posting in job_postings:
        print(job_posting["title"])
        print(job_posting["company"])
        print(job_posting["location"])

if __name__ == "__main__":
    job_postings = get_job_postings()
    show_job_postings(job_postings)
