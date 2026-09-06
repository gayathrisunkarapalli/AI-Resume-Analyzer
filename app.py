import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import calculate_matches
from roadmap_generator import find_missing_skills, generate_roadmap

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer & Job Recommendation System")
st.write(
    "Upload a resume to analyze skills, recommend suitable job roles, "
    "identify skill gaps, and generate a learning roadmap."
)
st.divider()

st.header("📄 Upload Your Resume")
uploaded_file = st.file_uploader(
    "Choose a PDF or DOCX resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    with st.spinner("Reading your resume..."):
        resume_text = extract_resume_text(uploaded_file)

    if not resume_text.strip():
        st.error("Could not extract text from this resume.")
        st.stop()

    cleaned_text = clean_text(resume_text)
    skills = extract_skills(cleaned_text)

    st.divider()
    st.header("🔍 Skills Detected")
    if skills:
        cols = st.columns(4)
        for index, skill in enumerate(skills):
            with cols[index % 4]:
                st.success(skill.title())
    else:
        st.warning("No skills were detected in the resume.")

    st.divider()
    st.header("🎯 Job Role Matching")
    with st.spinner("Calculating job-role matches..."):
        matches = calculate_matches(cleaned_text)

    match_df = pd.DataFrame(matches)
    st.subheader("Resume Match Scores")
    st.dataframe(match_df, use_container_width=True, hide_index=True)

    st.subheader("📊 Match Score Chart")
    chart_df = match_df.sort_values("Match Score")
    fig = px.bar(
        chart_df,
        x="Match Score",
        y="Job Role",
        orientation="h",
        title="Resume vs Job Role Match"
    )
    fig.update_layout(
        xaxis_title="Match Score (%)",
        yaxis_title="Job Role"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.header("🏆 Top 3 Recommended Roles")
    top_roles = matches[:3]
    cols = st.columns(3)
    for index, role in enumerate(top_roles):
        with cols[index]:
            st.metric(
                label=role["Job Role"],
                value=f'{role["Match Score"]}%'
            )

    st.divider()
    st.header("🎯 Analyze a Target Role")
    job_roles = [item["Job Role"] for item in matches]
    target_role = st.selectbox(
        "Select the job role you want to target:",
        job_roles
    )

    missing_skills = find_missing_skills(skills, target_role)

    st.subheader("⚠️ Skill Gap Analysis")
    if missing_skills:
        st.write("Skills you may need to develop:")
        for skill in missing_skills:
            st.warning(f"❌ {skill.title()}")
    else:
        st.success("🎉 No major skill gaps detected!")

    st.divider()
    st.header("📚 Personalized Learning Roadmap")
    roadmap = generate_roadmap(missing_skills)
    if roadmap:
        for step in roadmap:
            st.info(step)
    else:
        st.success("You already have the major skills required for this role.")

    st.divider()
    with st.expander("📃 View Extracted Resume Text"):
        st.text_area("Extracted text", resume_text, height=300)

    st.divider()
    st.info(
        "**Responsible AI Notice**\n\n"
        "Match scores are estimates intended for career guidance. "
        "They should not be used for automatic hiring or rejection decisions. "
        "The system evaluates job-related information such as skills and resume content."
    )
else:
    st.info("👆 Upload a PDF or DOCX resume to begin.")
