import pandas as pd
from data_loader import load_candidates, load_job_description
from scoring import model, build_candidate_text, semantic_score, skill_score, experience_score, behavioral_score

# Load data
candidates = load_candidates("path_to_candidates.json")
job_description = load_job_description()

# Precompute JD embedding
jd_embedding = model.encode([job_description], normalize_embeddings=True)

# Prepare candidate data
results = []
for candidate in candidates:
    candidate_embedding = model.encode([build_candidate_text(candidate)], normalize_embeddings=True)
    sem_score = semantic_score(jd_embedding, candidate_embedding)
    skill_score_val = skill_score(candidate, must_have_skills=["Python", "Embeddings", "FAISS", "Retrieval"])
    exp_score = experience_score(candidate)
    beh_score = behavioral_score(candidate)
    
    # You can adjust weights as needed
    final_score = (0.35 * sem_score + 0.25 * skill_score_val + 0.15 * exp_score + 0.15 * beh_score)
    
    results.append((candidate["candidate_id"], final_score, candidate))

# Rank candidates by final score
ranked = sorted(results, key=lambda x: x[1], reverse=True)

# Output top 100 (example: print or save)
top_100 = ranked[:100]
df = pd.DataFrame(top_100, columns=["candidate_id", "score", "candidate_info"])
df.to_csv("top_100_candidates.csv", index=False)
