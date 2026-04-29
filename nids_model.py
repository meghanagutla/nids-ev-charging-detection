import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (mock structure)
data = {
    "packet_size": [500, 1500, 300, 2000],
    "duration": [1, 5, 1, 10],
    "label": [0, 1, 0, 1]  # 0 = normal, 1 = attack
}

df = pd.DataFrame(data)

# Features & target
X = df[["packet_size", "duration"]]
y = df["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully")
