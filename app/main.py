from app.parsers import parse_resume
from app.preprocessor import preprocess_text
from app.heuristics import analyze_resume
from app.matcher import calculate_match_score, find_missing_keywords
from app.advisor import get_resume_advice
from database.db_manager import (
    create_database,
    save_result,
    get_results
)

import streamlit as st

create_database()

st.title("AI Resume Analyzer")

st.write("Upload Resume and Check ATS Score")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description Here"
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        resume_text = parse_resume(uploaded_file)

        clean_resume = preprocess_text(resume_text)

        clean_job = preprocess_text(job_description)

        score = calculate_match_score(
            clean_resume,
            clean_job
        )

        missing = find_missing_keywords(
            clean_resume,
            clean_job
        )

        st.success("Analysis Complete")
        
        save_result(
            "Candidate",
            score
        )
        st.metric(
            "ATS Score",
            f"{score}%"
        )
        heuristics = analyze_resume(
            resume_text
        )

        advice = get_resume_advice(
            resume_text,
            job_description
        )

        st.write("Heuristics Result:")
        st.write(heuristics)

        st.write("Missing Skills:")
        st.write(missing)

        st.subheader("AI Suggestions")
        st.info(advice)

    else:

        st.warning(
            "Upload Resume and Job Description"
        )
            
st.subheader("Analysis History")
      
history = get_results()
        
for row in history:
    st.write(row)