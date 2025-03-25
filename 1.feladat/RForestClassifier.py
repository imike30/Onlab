import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.multioutput import MultiOutputClassifier

train_data = pd.read_csv("network_data.csv")
test_data = pd.read_csv("test_data.csv")

X_train = train_data.iloc[:, :-6]
y_train = train_data.iloc[:, -6:]

X_test = test_data.iloc[:, :-6]
y_test = test_data.iloc[:, -6:]

model = RandomForestClassifier(n_estimators=100, random_state=42)

multi_target_rf = MultiOutputClassifier(model)

multi_target_rf.fit(X_train, y_train)

y_pred = multi_target_rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", report)
