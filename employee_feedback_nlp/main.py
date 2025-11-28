import data_loader
import analyzer
import topic_extractor
import summarizer
import recommender
import sys

def main():
    print("Initializing Employee Feedback NLP Pipeline...")
    
    # 1. Load Data
    messages = data_loader.get_feedback_data()
    print(f"Loaded {len(messages)} messages.\n")
    
    # 2. Extract Global Topics
    print("Extracting Global Topics...")
    global_topics = topic_extractor.extract_topics(messages)
    print(f"Top Topics: {', '.join(global_topics)}\n")
    
    print("-" * 50)
    print("INDIVIDUAL MESSAGE ANALYSIS")
    print("-" * 50)
    
    for i, msg in enumerate(messages):
        print(f"\nMessage {i+1}:")
        print(f"Original: \"{msg}\"")
        
        # 3. Sentiment & Stress
        sentiment = analyzer.analyze_sentiment(msg)
        stress = analyzer.estimate_stress(msg)
        print(f"Sentiment Score: {sentiment:.2f}")
        print(f"Stress Level: {stress:.2f}")
        
        # 4. Keywords
        keywords = topic_extractor.extract_keywords(msg)
        print(f"Keywords: {', '.join(keywords)}")
        
        # 5. Summary
        summary = summarizer.summarize_text(msg)
        print(f"Summary: {summary}")
        
        # 6. Recommendations
        tags = recommender.get_recommendations(sentiment, stress, msg)
        print(f"HR Tags: {tags}")
        print("-" * 30)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
