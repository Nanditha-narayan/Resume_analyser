import spacy
from pdfminer.high_level import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
import pymongo

# Load Spacy NLP Model
nlp = spacy.load('en_core_web_sm')

def parse_resume(file_path):
    """Extracts text from a PDF resume and extracts keywords using NLP."""
    try:
        text = extract_text(file_path).strip()
        if not text:
            print("Warning: Extracted text is empty.")
            return []

        doc = nlp(text)
        keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        return keywords
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return []

def match_with_jobs(resume_keywords, job_domain):
    """Compares extracted resume keywords with job descriptions in MongoDB."""
    try:
        with pymongo.MongoClient("mongodb://localhost:27017/") as client:
            db = client["job_db"]
            job_desc = db["jobs"].find_one({"domain": job_domain})  # Fetch job description

            if not job_desc:
                print(f"Warning: No job description found for domain: {job_domain}")
                return 0  # No match if job description is missing

            job_text = job_desc.get('description', '')
            if not job_text:
                print(f"Warning: Job description is empty for domain: {job_domain}")
                return 0

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([" ".join(resume_keywords), job_text])
            similarity = (vectors * vectors.T).toarray()[0, 1] * 100

            return round(similarity, 2)  # Return similarity percentage
    except Exception as e:
        print(f"Error in job matching: {e}")
        return 0
