from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(input_features, description_features):
    # Example: Using cosine similarity for similarity calculation
    similarity_scores = cosine_similarity(input_features, description_features)

    return similarity_scores
