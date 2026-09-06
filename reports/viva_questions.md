# Viva Questions and Short Answers

### 1. What is the objective of the project?
To analyze resumes, identify skills, recommend suitable job roles, find skill gaps, and provide a learning roadmap.

### 2. Why is pypdf used?
It extracts text from PDF resumes.

### 3. Why is python-docx used?
It extracts text from DOCX resumes.

### 4. What is TF-IDF?
TF-IDF is a text-vectorization technique that gives higher importance to terms that are frequent in one document but less common across documents.

### 5. What is cosine similarity?
It measures similarity between two vectors using the cosine of the angle between them.

### 6. Why use a skill dictionary?
It provides a controlled list of job-related skills for consistent extraction.

### 7. What are the limitations of keyword matching?
It can miss synonyms, abbreviations, context, and skills described without the exact keyword.

### 8. Why use Streamlit?
It provides a simple way to build an interactive Python web dashboard.

### 9. How are missing skills found?
The required skills for the selected role are compared with the skills detected in the resume.

### 10. Is the match score a hiring decision?
No. It is only an estimated career-guidance score.

### 11. What could improve the NLP component?
Sentence Transformer embeddings, better synonym handling, and section-aware parsing could improve semantic matching.

### 12. What is responsible AI in this project?
The system should use job-related information and must not make automated hiring/rejection decisions based on unrelated or protected personal attributes.
