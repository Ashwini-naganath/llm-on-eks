import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCUMENT_DIR = os.path.join(os.path.dirname(__file__), "documents")

documents = []
filenames = []

for filename in os.listdir(DOCUMENT_DIR):
    filepath = os.path.join(DOCUMENT_DIR, filename)

    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            documents.append(f.read())
            filenames.append(filename)

vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(documents)


def retrieve_context(query, k=2):
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    top_indices = similarities.argsort()[-k:][::-1]

    results = []

    for index in top_indices:
        results.append(documents[index])

    return "\n\n".join(results)
