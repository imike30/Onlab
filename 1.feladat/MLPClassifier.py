import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

train_data = pd.read_csv("network_data.csv")
test_data = pd.read_csv("test_data.csv")

X_train = train_data.iloc[:, :-7]
y_train = train_data.iloc[:, -7:]

X_test = test_data.iloc[:, :-7]
y_test = test_data.iloc[:, -7:]

y_train = y_train.idxmax(axis=1)
y_test = y_test.idxmax(axis=1)

label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train_encoded)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test_encoded, y_pred)
report = classification_report(y_test_encoded, y_pred, target_names=label_encoder.classes_)

print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", report)
