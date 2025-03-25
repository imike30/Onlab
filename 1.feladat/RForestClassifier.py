import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.multioutput import MultiOutputClassifier

# Betöltjük az adathalmazokat
train_data = pd.read_csv("network_data.csv")  # Tanító adathalmaz
test_data = pd.read_csv("test_data.csv")    # Teszt adathalmaz

# Separate features (X) and target labels (y)
X_train = train_data.iloc[:, :-6]  # Traffic data
y_train = train_data.iloc[:, -6:]  # Failure labels (one-hot encoded)

X_test = test_data.iloc[:, :-6]
y_test = test_data.iloc[:, -6:]

# Létrehozzuk és betanítjuk a Random Forest modellt
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Multi-output osztályozó létrehozása
multi_target_rf = MultiOutputClassifier(model)

multi_target_rf.fit(X_train, y_train)

# Előrejelzés a teszt adatokon
y_pred = multi_target_rf.predict(X_test)

# Kiértékelés
accuracy = accuracy_score(y_test, y_pred)
print(f"🌟 Modell pontossága: {accuracy:.4f}\n")
print("📊 Osztályozási jelentés:\n", classification_report(y_test, y_pred))
