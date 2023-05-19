from scraping.scraper import scrape_clothing_descriptions
from preprocessing.cleaner import clean_text
from similarity.feature_extraction import extract_features
from similarity.similarity_calculation import calculate_similarity
from ranking.ranker import rank_items


def clothing_similarity_search(input_text, top_n):
    # Step 1: Scrape clothing item descriptions
    clothing_descriptions = scrape_clothing_descriptions()

    # Step 2: Preprocess the text data
    cleaned_input_text = clean_text(input_text)
    cleaned_descriptions = [clean_text(desc) for desc in clothing_descriptions]

    # Step 3: Extract features and compute similarity
    input_features = extract_features(cleaned_input_text)
    description_features = [extract_features(desc) for desc in cleaned_descriptions]
    similarity_scores = calculate_similarity(input_features, description_features)

    # Step 4: Rank the results
    ranked_results = rank_items(clothing_descriptions, similarity_scores, top_n)

    return ranked_results


if __name__ == '__main__':
    input_text = "This is a description of a clothing item."
    top_n = 5

    results = clothing_similarity_search(input_text, top_n)

    print("Top {} similar clothing items:".format(top_n))
    for i, result in enumerate(results, 1):
        print("{}. {} - {}".format(i, result['title'], result['url']))
