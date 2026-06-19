import streamlit as st
from data_loader import load_candidates, load_job_description
from ranker import ranked  # Assuming ranker.py final ranking logic

st.title("Candidate Ranking System")

uploaded_file = st.file_uploader("Upload Candidates JSON", type="json")

if uploaded_file:
    candidates = load_candidates(uploaded_file)
    jd = load_job_description()  

    st.write("Job Description:", jd)

    # Reuse the ranking logic
    top_100 = ranked  # Use the ranking results from ranker.py

    st.subheader("Top 100 Candidates")
    for rank, (cid, score, candidate) in enumerate(top_100, start=1):
        st.write(f"Rank {rank}: {candidate['profile']['anonymized_name']} (ID: {cid}) - Score: {score:.4f}")
