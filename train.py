
import os
from utilities.data_loader import load_data
from utilities.model import train_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

iscx_path = os.path.join(BASE_DIR, "datasets", "ISCX-URL-2016.csv")
phish_path = os.path.join(BASE_DIR, "datasets", "Phish_Storm.csv")

data = load_data(iscx_path, phish_path)

train_model(data)

print("Model trained successfully!")
