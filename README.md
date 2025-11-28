# Employee Feedback NLP Analysis

A mini NLP project to analyze employee feedback messages for sentiment, stress, topics, and HR recommendations.

## Features
- **Sentiment Analysis**: Uses VADER to determine positive/negative sentiment.
- **Stress Estimation**: Heuristic-based detection of burnout and stress keywords.
- **Topic Extraction**: Uses NMF and TF-IDF to find key themes.
- **Summarization**: Extractive summarization using LSA (via Sumy).
- **HR Recommendations**: Auto-tags feedback with actionable labels (e.g., "Wellness Check", "Kudos").

## Setup

### Prerequisites
- Python 3.8+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SepehrRezaee/employee_feedback_nlp.git
   cd employee_feedback_nlp
   ```

2. **Create a Virtual Environment**

   *Windows:*
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   *Note: If you get a permission error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.*

   *Mac/Linux:*
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: If `requirements.txt` is missing, install manually: `pip install textblob vaderSentiment scikit-learn sumy nltk numpy`)*

4. **Download NLTK Data**
   The script should handle this, but if you see errors:
   ```bash
   python -m nltk.downloader punkt
   ```

## Usage

Run the main analysis script:

```bash
python main.py
```

## Project Structure
- `data_loader.py`: Contains sample feedback data.
- `analyzer.py`: Sentiment and stress analysis logic.
- `topic_extractor.py`: Topic modeling and keyword extraction.
- `summarizer.py`: Text summarization.
- `recommender.py`: Rule-based HR tagging.
- `main.py`: Main execution script.

## Output Example
```text
Message: "The deadline for the Q4 report is impossible. I'm stressed..."
Sentiment Score: -0.50
Stress Level: 0.90
HR Tags: ['URGENT: Wellness Check']
```
