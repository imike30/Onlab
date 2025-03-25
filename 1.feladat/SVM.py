import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load training and test data
train_data = pd.read_csv("network_data.csv")
test_data = pd.read_csv("test_data.csv")

# Separate features (X) and target labels (y)
X_train = train_data.iloc[:, :-6]  # Traffic data
y_train = train_data.iloc[:, -6:]  # Failure labels (one-hot encoded)

X_test = test_data.iloc[:, :-6]
y_test = test_data.iloc[:, -6:]

# Convert one-hot encoded labels to a single categorical label
y_train = y_train.idxmax(axis=1)
y_test = y_test.idxmax(axis=1)

# Encode categorical labels into numerical values
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Normalize the input features
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train the SVM model
model = SVC(kernel='rbf', C=10.0, gamma='scale')  # Radial Basis Function kernel
model.fit(X_train_scaled, y_train_encoded)

# Predict on the test set
y_pred = model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test_encoded, y_pred)
report = classification_report(y_test_encoded, y_pred, target_names=label_encoder.classes_)

print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", report)
