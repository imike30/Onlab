import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Load the dataset
train_data = pd.read_csv("network_data.csv")

# Separate features (X) and labels (y)
X_train = train_data.iloc[:, :-6]  # All traffic columns
y_train = train_data.iloc[:, -6:]  # Binary failure columns

# Convert labels to a single categorical output (index of failure type)
y_train = y_train.idxmax(axis=1)  # Get the failure type as a single categorical value

# Convert string labels to numerical values
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)  # Convert labels to integers

# Load test data (features only)
test_data = pd.read_csv("test_data.csv")

# Separate features (X) and labels (y) in the test set
X_test = test_data.iloc[:, :-6]  # Traffic data
y_test = test_data.iloc[:, -6:]  # Binary failure labels

# Convert one-hot encoded labels to categorical labels
y_test = y_test.idxmax(axis=1)

# Encode labels numerically using the same encoder as training
y_test = label_encoder.transform(y_test)

# Create an XGBoost classifier model
model = xgb.XGBClassifier(
    objective="multi:softmax",  # Multi-class classification
    num_class=6,  # Number of failure classes (including "semmi")
    eval_metric="mlogloss",
    use_label_encoder=False
)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
