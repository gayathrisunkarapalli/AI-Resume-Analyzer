import pandas as pd

def find_missing_skills(extracted_skills, target_role):
    jobs = pd.read_csv("data/job_roles.csv")
    row = jobs[jobs["job_role"] == target_role]

    if row.empty:
        return []

    required = row.iloc[0]["required_skills"].lower().split(",")
    required = [skill.strip() for skill in required]

    extracted = {skill.lower() for skill in extracted_skills}
    return [skill for skill in required if skill not in extracted]

def generate_roadmap(missing_skills):
    roadmap = []

    for index, skill in enumerate(missing_skills[:6], start=1):
        roadmap.append(
            f"Week {index}: Learn {skill.title()} and build a small project."
        )

    return roadmap
