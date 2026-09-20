import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/tickets.csv")

# Input
X = df["message"]

# Targets
y_category = df["category"]
y_priority = df["priority"]

# Split dataset for category model
X_train, X_test, y_category_train, y_category_test = train_test_split(
    X,
    y_category,
    test_size=0.2,
    random_state=42,
    stratify=y_category
)

# Split dataset for priority model
X_priority_train, X_priority_test, y_priority_train, y_priority_test = train_test_split(
    X,
    y_priority,
    test_size=0.2,
    random_state=42,
    stratify=y_priority
)

# Convert category text into numbers
category_vectorizer = TfidfVectorizer()

X_category_train = category_vectorizer.fit_transform(X_train)
X_category_test = category_vectorizer.transform(X_test)

# Train category model
category_model = LogisticRegression(max_iter=1000)

category_model.fit(
    X_category_train,
    y_category_train
)

# Predict category
category_predictions = category_model.predict(X_category_test)

category_accuracy = accuracy_score(
    y_category_test,
    category_predictions
)

print("Category Model Accuracy:", category_accuracy)


# Convert priority text into numbers
priority_vectorizer = TfidfVectorizer()

X_priority_train_vectorized = priority_vectorizer.fit_transform(
    X_priority_train
)

X_priority_test_vectorized = priority_vectorizer.transform(
    X_priority_test
)

# Train priority model
priority_model = LogisticRegression(max_iter=1000)

priority_model.fit(
    X_priority_train_vectorized,
    y_priority_train
)

# Predict priority
priority_predictions = priority_model.predict(
    X_priority_test_vectorized
)

priority_accuracy = accuracy_score(
    y_priority_test,
    priority_predictions
)

print("Priority Model Accuracy:", priority_accuracy)


# Test a completely new ticket
new_ticket = [
    "My bank account was charged but my order didn't go through."
]

# Category prediction
new_category_vector = category_vectorizer.transform(new_ticket)

predicted_category = category_model.predict(
    new_category_vector
)

# Priority prediction
new_priority_vector = priority_vectorizer.transform(new_ticket)

predicted_priority = priority_model.predict(
    new_priority_vector
)

print("\nNew Ticket:")
print(new_ticket[0])

print("Predicted Category:", predicted_category[0])
print("Predicted Priority:", predicted_priority[0])

print("Predicted Priority:", predicted_priority[0])

# Save trained models
import joblib

joblib.dump(category_model, "model/category_model.pkl")
joblib.dump(category_vectorizer, "model/category_vectorizer.pkl")

joblib.dump(priority_model, "model/priority_model.pkl")
joblib.dump(priority_vectorizer, "model/priority_vectorizer.pkl")

print("\nModels saved successfully!")