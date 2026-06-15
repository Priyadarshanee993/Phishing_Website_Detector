import pandas as pd
from utilities.model import load_model, extract_features

def predict_urls(urls):
    model = load_model() 
    features = [extract_features(url) for url in urls]
    predictions = model.predict(features)
    return predictions

if __name__ == "__main__":
    
    test_urls = [
    'https://www.google.com',
    'https://www.wikipedia.org',
    'https://github.com',
    'https://www.microsoft.com',
    'https://www.amazon.in'
]  # Thay đổi với các URL của bạn
    results = predict_urls(test_urls)
    
    for url, result in zip(test_urls, results):
        label = "Phishing" if result == 1 else "Legitimate"
        print(f'URL: {url} - {label}')