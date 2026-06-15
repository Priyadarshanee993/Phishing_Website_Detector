import pickle
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def extract_features(url):
    """
    Extract features from a URL.
    """

    return [
        len(url),              # URL length
        url.count('.'),        # Number of dots
        url.count('/'),        # Number of slashes
        url.count('-'),        # Number of hyphens
        url.count('@'),        # Number of @ symbols
        url.count('?'),        # Number of question marks
        url.count('='),        # Number of equal signs
        url.count('%'),        # Number of % symbols
        int('https' in url),   # Uses HTTPS
        int('www' in url)      # Contains www
    ]


def train_model(data):
    """
    Train the phishing detection model and save it.
    """

    X = data['url'].apply(extract_features).tolist()
    y = data['label']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        eval_metric='logloss'
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model


def load_model():
    """
    Load the saved model.
    """

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    return model
