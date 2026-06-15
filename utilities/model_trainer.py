import os
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

from utilities.data_loader import load_data
from utilities.model import extract_features


def train_model():
    # Get project root directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    iscx_path = os.path.join(BASE_DIR, "datasets", "ISCX-URL-2016.csv")
    phish_path = os.path.join(BASE_DIR, "datasets", "Phish_Storm.csv")

    data = load_data(iscx_path, phish_path)

    X = data['url'].apply(extract_features).tolist()
    y = data['label'].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBClassifier()
    model.fit(X_train, y_train)

    return model