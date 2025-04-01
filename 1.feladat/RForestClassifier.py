import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.multioutput import MultiOutputClassifier

train_data = pd.read_csv("network_data.csv")
test_data = pd.read_csv("test_data.csv")

X_train = train_data.iloc[:, :-7]
y_train = train_data.iloc[:, -7:]

X_test = test_data.iloc[:, :-7]
y_test = test_data.iloc[:, -7:]

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    max_depth=10,
    max_features=6,
    min_samples_leaf=5
    )

multi_target_rf = MultiOutputClassifier(model)

multi_target_rf.fit(X_train, y_train)

y_pred = multi_target_rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", report)
