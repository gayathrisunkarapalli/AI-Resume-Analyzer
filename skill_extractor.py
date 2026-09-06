import re
import pandas as pd

def load_skills():
    skills_df = pd.read_csv("data/skill_dictionary.csv")
    return skills_df["skill"].str.lower().tolist()

def extract_skills(resume_text):
    skill_list = load_skills()
    detected_skills = []
    text = resume_text.lower()

    for skill in skill_list:
        pattern = r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
        if re.search(pattern, text):
            detected_skills.append(skill)

    return sorted(set(detected_skills))
