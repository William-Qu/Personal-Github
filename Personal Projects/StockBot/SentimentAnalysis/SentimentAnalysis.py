import feedparser
import requests
from bs4 import BeautifulSoup
#from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#from datetime import datetime
from urllib.parse import quote

from transformers import AutoTokenizer, AutoModelForSequenceClassification
#from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertForSequenceClassification, BertTokenizer, BertConfig
import torch
import numpy as np
from googlenewsdecoder import gnewsdecoder




###!!!TODO: WHY ARE THERE SO MANY POLARITY 0 REPORTS?

#model_name = "yiyanghkust/finbert-tone"
model_name = '9mark9/finbert-deberta-large-sentiment'

#config = BertConfig.from_pretrained(model_name)
#
#finbert_tokenizer = BertTokenizer.from_pretrained(model_name)
#
#finbert_model = BertForSequenceClassification.from_pretrained(
#    model_name,
#    config=config
#)


finbert_model = AutoModelForSequenceClassification.from_pretrained(model_name)
finbert_tokenizer = AutoTokenizer.from_pretrained(model_name)

labels = ['Positive', 'Negative', 'Neutral']

def fetch_news(query, num_articles=10):
    rss_url = f"https://news.google.com/rss/search?q={quote(query)}"
    feed = feedparser.parse(rss_url)
    news_items = feed.entries[:num_articles]

    articles = []
    for item in news_items:
        title = item.title
        link = item.link
        published = item.published
        content = fetch_article_content(link)
        
        articles.append({
            "title": title,
            "link": link,
            "published": published,
            "content": content
        })

    return articles

def fetch_article_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()        
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content.strip()
    except requests.RequestException:
        return "Content not retrieved."



def analyze_sentiment(text):

    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    polarity = scores['compound']

    # analysis = TextBlob(text)
    # polarity = analysis.sentiment.polarity

    
    if polarity > 0.03:
        sentiment = 'Positive'
    elif polarity < -0.03:
        sentiment = 'Negative'
    else:
        print(f'Polarity: {polarity}')
        print(f'Text: {text}')
        sentiment = 'Neutral'

    return polarity, sentiment

# def analyze_sentiment(text):
#     if not text.strip():
#         return 0.0, 'Neutral'

#     inputs = finbert_tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
#     with torch.no_grad():
#         outputs = finbert_model(**inputs)

#     logits = outputs.logits
#     probabilities = torch.softmax(logits, dim=1).numpy()[0]
#     max_index = np.argmax(probabilities)
#     sentiment = labels[max_index]
#     confidence = probabilities[max_index]

#     return confidence, sentiment




def summarize_sentiments(articles):
    summary = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }

    for article in articles:
        # print("-"*25)
        # print(f"\n--- Analyzing Article: {article['title']} ---")
        # print(f"Published: {article['published']}")
        # print(article['content'])
        #_, sentiment = analyze_sentiment(article['title'] + " # " + article['content'])
        _, sentiment = analyze_sentiment(article['title'])

        if sentiment == 'Neutral':
            print(article['link'])
    
        summary[sentiment] += 1

    total = len(articles)
    print("\n--- Market Sentiment Summary ---")
    print(f"Total articles analyzed: {total}")
    
    purchase_percent = 0.5
    for sentiment, count in summary.items():
        percent = (count / total) * 100
        print(f"{sentiment}: {count} ({percent:.2f}%)")
        
        if sentiment == 'Positive':
            purchase_percent += 0.5 * (count / total)
        elif sentiment == 'Negative':
            purchase_percent -= 0.5 * (count / total)
    
    print(f"The recommendation percent of purchase is: {purchase_percent * 100: .2f}")





def main():
    #queries = [
    #    "gold market",
    #    "gold price",
    #    "gold news",
    #    "gold trends",
    #    "gold analysis",
    #    "gold forecast",
    #    "gold investment"
    #]
    
    # Potentially seperate sentiment analysis into three categories:
        # 1) Macroeconomic sentiment: Federal Reserve, Inflation, Interest Rates, US Economy, Unemployment.
        # 2) Market sentiment: Stock Market, Market Crash, Investor Sentiment.
        # 3) Risk sentiment: Geopolitical Risk, Corporate Earnings.
    queries = [
    "Stock Market",
    "Federal Reserve",
    "Inflation",
    "Interest Rates",
    "US Economy",
    "Market Crash",
    "Corporate Earnings",
    "Geopolitical Risk",
    "Unemployment",
    "Investor Sentiment"
    ]

    
    num_articles_per_query = 1
    all_articles = []

    for query in queries:
        print(f"Fetching news articles for '{query}'...\n")
        articles = fetch_news(query, num_articles_per_query)
        all_articles.extend(articles)

    #for idx, article in enumerate(all_articles, 1):
        #print(f"Article {idx}: {article['title']}")
        #print(f"Link: {article['link']}")
        #print(f"Published: {article['published']}")

        #polarity, sentiment = analyze_sentiment(str(article['title']) + ' # ' + str(article['content']))  # or article['title']
        #print(f"Sentiment: {sentiment} (Polarity: {polarity:.2f})\n")

    summarize_sentiments(all_articles)

if __name__ == "__main__":
    main()