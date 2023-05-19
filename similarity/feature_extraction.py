from sklearn.feature_extraction.text import TfidfVectorizer


def extract_features(text):
    # Example: Using TF-IDF for feature extraction
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(text)

    return features


def extract_features_batch(text_list):
    # Example: Using TF-IDF for feature extraction on a batch of texts
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform(text_list)

    return features
