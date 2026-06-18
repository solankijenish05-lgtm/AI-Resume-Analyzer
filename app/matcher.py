from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_vectors(resume_text, job_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [resume_text, job_text]
    )

    return vectors


def calculate_match_score(resume_text, job_text):

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(
        [resume_text, job_text]
    )

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)


def find_missing_keywords(resume_text, job_text):

    resume_words = set(
        resume_text.lower().split()
    )

    job_words = set(
        job_text.lower().split()
    )

    missing = job_words - resume_words

    return list(missing)