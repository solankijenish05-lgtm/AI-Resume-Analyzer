import streamlit as st

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
    st.success("Analysis Started")

st.metric("ATS Score", "85%")

tab1, tab2, tab3 = st.tabs(
    ["ATS Score", "Missing Skills", "AI Suggestions"]
)

with tab1:
    st.metric("ATS Score", "85%")

with tab2:
    st.write("Docker")
    st.write("Machine Learning")

with tab3:
    st.write("Add more projects")
    st.write("Improve summary")