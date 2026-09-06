# Project Report
## AI Resume Analyzer and Job Recommendation System

### Abstract
The AI Resume Analyzer and Job Recommendation System is a career-guidance application that uses natural-language processing techniques to analyze resumes and compare them with predefined job-role requirements. The system extracts text from PDF and DOCX files, cleans the text, identifies technical skills, calculates role similarity using TF-IDF and cosine similarity, recommends suitable roles, identifies missing skills, and generates a learning roadmap.

### Objectives
- Automate basic resume text extraction and analysis.
- Identify technical skills from resume content.
- Recommend suitable job roles.
- Highlight skill gaps.
- Provide a simple learning roadmap.
- Present results through an interactive Streamlit dashboard.

### Modules
1. Resume upload and validation
2. PDF/DOCX text extraction
3. Text cleaning
4. Skill extraction
5. Job-role matching
6. Recommendation
7. Skill-gap analysis
8. Learning roadmap
9. Streamlit presentation layer

### Algorithms
**TF-IDF:** Represents text using term frequency and inverse document frequency.

**Cosine Similarity:** Measures the angle-based similarity between the resume vector and job-role vector.

**Keyword/Regex Skill Matching:** Checks whether skills from the controlled dictionary occur in the cleaned resume text.

### Output
The application displays detected skills, match scores for available roles, a chart, the top three recommended roles, missing skills for a selected role, and a learning roadmap.

### Testing
The application was tested using PDF and DOCX sample resumes, including successful text extraction, skill detection, role matching, and roadmap generation.

### Limitations
The system is an educational prototype. Keyword matching may miss equivalent terminology, and TF-IDF does not provide full semantic understanding. Scores are estimates and should not be interpreted as hiring decisions.

### Conclusion
The project demonstrates how NLP preprocessing, controlled skill extraction, vector-space similarity, and rule-based recommendations can be combined into a practical Streamlit career-guidance application.
