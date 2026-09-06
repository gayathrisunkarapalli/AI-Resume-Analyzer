import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_job_roles():
    return pd.read_csv("data/job_roles.csv")

def calculate_matches(resume_text):
    jobs = load_job_roles()
    results = []

    for _, row in jobs.iterrows():
        role = row["job_role"]
        required_skills = row["required_skills"]
        documents = [resume_text, required_skills]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        score = round(similarity * 100, 2)

        results.append({
            "Job Role": role,
            "Match Score": score
        })

    results.sort(key=lambda x: x["Match Score"], reverse=True)
    return results
