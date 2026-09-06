# System Architecture

```text
                    ┌──────────────────────┐
                    │   User uploads       │
                    │   PDF / DOCX resume  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Resume Parser      │
                    │   pypdf / python-docx│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Text Cleaner       │
                    │   lowercase / regex  │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
       ┌────────────────────┐     ┌────────────────────┐
       │ Skill Extractor    │     │ TF-IDF Matcher     │
       │ skill dictionary   │     │ + cosine similarity│
       └─────────┬──────────┘     └─────────┬──────────┘
                 │                          │
                 └────────────┬─────────────┘
                              ▼
                    ┌──────────────────────┐
                    │ Job Role Results     │
                    │ Top 3 recommendations│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Skill Gap Analysis   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Learning Roadmap     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    └──────────────────────┘

Data files:
- data/skill_dictionary.csv
- data/job_roles.csv
```
