import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_db"]
jobs = db["jobs"]

job_data = [
    {"domain": "Software Engineering", "description": "Looking for Python and Django expertise with REST API knowledge."},
    {"domain": "Data Science", "description": "Experience in Machine Learning, NLP, and Python required."},
]

result = jobs.insert_many(job_data)
print(f"Inserted {len(result.inserted_ids)} job descriptions successfully!")
