from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

def extract_topics(texts, n_topics=3):
    if not texts:
        return []
        
    # Use TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(texts)
    
    # Use NMF for topic modeling
    nmf = NMF(n_components=n_topics, random_state=1, init='nndsvd').fit(tfidf)
    
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    topics = []
    for topic_idx, topic in enumerate(nmf.components_):
        top_features_ind = topic.argsort()[:-4:-1] # Top 3 words
        topic_words = [feature_names[i] for i in top_features_ind]
        topics.append(" ".join(topic_words))
        
    return topics

def extract_keywords(text):
    from sklearn.feature_extraction.text import CountVectorizer
    try:
        cv = CountVectorizer(stop_words='english', max_features=3)
        cv.fit([text])
        return list(cv.vocabulary_.keys())
    except:
        return []
