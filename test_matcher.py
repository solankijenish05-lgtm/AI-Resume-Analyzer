from app.matcher import (
    create_vectors,
    calculate_match_score,
    find_missing_keywords
)

resume = "Python Java SQL"
job = "Python SQL Docker"

vectors = create_vectors(
    resume,
    job
)

print("Vectors:")
print(vectors.toarray())

score = calculate_match_score(
    resume,
    job
)

print("Match Score:", score)

missing = find_missing_keywords(
    resume,
    job
)

print("Missing Skills:", missing)
