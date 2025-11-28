def get_recommendations(sentiment_score, stress_score, text):
    tags = []
    
    # Stress based tags
    if stress_score > 0.7:
        tags.append("URGENT: Wellness Check")
    elif stress_score > 0.4:
        tags.append("Monitor Workload")
        
    # Sentiment based tags
    if sentiment_score > 0.5:
        tags.append("Kudos")
    elif sentiment_score < -0.5:
        tags.append("Manager Intervention")
        
    # Content based tags (simple keyword matching)
    lower_text = text.lower()
    if "training" in lower_text or "learn" in lower_text:
        tags.append("L&D Opportunity")
    if "salary" in lower_text or "pay" in lower_text or "undervalued" in lower_text:
        tags.append("Compensation Review")
    if "policy" in lower_text:
        tags.append("Policy Feedback")
        
    if not tags:
        tags.append("General Feedback")
        
    return tags
