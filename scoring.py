from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_candidate_text(candidate):
    skills = " ".join(s["name"] for s in candidate["skills"])
    exp = " ".join(x["description"] for x in candidate["career_history"])
    edu = " ".join(e["field_of_study"] for e in candidate["education"])
    return f"{candidate['profile']['headline']}\n{candidate['profile']['summary']}\nSkills: {skills}\nExperience: {exp}\nEducation: {edu}"

def semantic_score(jd_embedding, candidate_embedding):
    return (candidate_embedding @ jd_embedding.T).item()

def skill_score(candidate, must_have_skills):
    candidate_skills = set(s["name"].lower() for s in candidate["skills"])
    matched = sum(1 for skill in must_have_skills if skill.lower() in candidate_skills)
    return matched / len(must_have_skills)

def experience_score(candidate, target_years=7):
    years = candidate["profile"]["years_of_experience"]
    return min(years / target_years, 1)

def behavioral_score(candidate):
    signals = candidate["redrob_signals"]
    score = 0
    score += 0.2 if signals["open_to_work_flag"] else 0
    score += signals["recruiter_response_rate"] * 0.2
    score += signals["interview_completion_rate"] * 0.2
    score += (min(signals["profile_completeness_score
