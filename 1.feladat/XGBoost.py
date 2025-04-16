import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

train_data = pd.read_csv("bigger_network_data_missing.csv")
test_data = pd.read_csv("bigger_test_data_missing.csv")

X_train = train_data.iloc[:, :-11]
y_train = train_data.iloc[:, -11:]

X_test = test_data.iloc[:, :-11]
y_test = test_data.iloc[:, -11:]

y_train = y_train.idxmax(axis=1)
y_test = y_test.idxmax(axis=1)

label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)
y_test = label_encoder.transform(y_test)

model = xgb.XGBClassifier(
    objective="multi:softmax",
    num_class=11,
    eval_metric="mlogloss",
    use_label_encoder=False
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

print(f"Model Accuracy: {accuracy:.4f}\n")
print("\nClassification Report:\n", report)
