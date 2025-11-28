from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    return score['compound']

def estimate_stress(text):
    # Heuristic: High stress if sentiment is negative and contains stress keywords
    stress_keywords = ['burnt out', 'burnout', 'stress', 'overwhelmed', 'deadline', 'tired', 'exhausted', 'impossible', 'working weekends', 'undervalued']
    
    sentiment = analyze_sentiment(text)
    blob = TextBlob(text)
    
    stress_score = 0.0
    if sentiment < -0.2:
        stress_score += 0.3
    if sentiment < -0.5:
        stress_score += 0.2
        
    lower_text = text.lower()
    for keyword in stress_keywords:
        if keyword in lower_text:
            stress_score += 0.2
            
    return min(stress_score, 1.0)
