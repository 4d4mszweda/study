import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import text2emotion as t2e
# from transformers import pipeline

nltk.download('vader_lexicon')

positive_review = (
    "This hotel was absolutely fantastic! The staff were incredibly friendly and helpful, "
    "the rooms were spotless, and the view from our balcony was breathtaking. "
    "I would definitely recommend this place to anyone looking for a relaxing getaway."
)

negative_review = (
    "This was the worst hotel experience I have ever had. The room was filthy, "
    "the staff were rude and unprofessional, and the food was inedible. "
    "I would never stay here again, and I suggest everyone avoid this place."
)

def analyze_with_vader(review):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(review)
    return scores

# def analyze_with_text2emotion(review):
#     emotions = t2e.get_emotion(review)
#     return emotions

def analyze_with_bert(review):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(review)
    return result

print("Positive Review Analysis:")
print("Vader:", analyze_with_vader(positive_review))
# print("Text2Emotion:", analyze_with_text2emotion(positive_review))
# print("BERT:", analyze_with_bert(positive_review))

print("\nNegative Review Analysis:")
print("Vader:", analyze_with_vader(negative_review))
# print("Text2Emotion:", analyze_with_text2emotion(negative_review))
# print("BERT:", analyze_with_bert(negative_review))
