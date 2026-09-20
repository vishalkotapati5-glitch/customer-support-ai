import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/tickets.csv")

print("Dataset loaded successfully!")
print("Total tickets:", len(df))


# ==========================================
# 2. INPUT AND TARGETS
# ==========================================

X = df["message"]

y_category = df["category"]

y_priority = df["priority"]


# ==========================================
# 3. SPLIT DATA FOR CATEGORY MODEL
# ==========================================

X_train, X_test, y_category_train, y_category_test = train_test_split(
    X,
    y_category,
    test_size=0.2,
    random_state=42,
    stratify=y_category
)


# ==========================================
# 4. SPLIT DATA FOR PRIORITY MODEL
# ==========================================

X_priority_train, X_priority_test, y_priority_train, y_priority_test = train_test_split(
    X,
    y_priority,
    test_size=0.2,
    random_state=42,
    stratify=y_priority
)


# ==========================================
# 5. CATEGORY MODEL
# ==========================================

category_vectorizer = TfidfVectorizer()

X_category_train = category_vectorizer.fit_transform(
    X_train
)

X_category_test = category_vectorizer.transform(
    X_test
)


category_model = LogisticRegression(
    max_iter=1000
)

category_model.fit(
    X_category_train,
    y_category_train
)


# ==========================================
# 6. CATEGORY PREDICTIONS
# ==========================================

category_predictions = category_model.predict(
    X_category_test
)


category_accuracy = accuracy_score(
    y_category_test,
    category_predictions
)

print("\n===================================")
print("CATEGORY MODEL")
print("===================================")

print(
    "Category Model Accuracy:",
    category_accuracy
)


# ==========================================
# 7. CATEGORY CLASSIFICATION REPORT
# ==========================================

print("\nCategory Classification Report:")

print(
    classification_report(
        y_category_test,
        category_predictions,
        zero_division=0
    )
)


# ==========================================
# 8. CATEGORY CONFUSION MATRIX
# ==========================================

category_labels = [
    "Account Issue",
    "Payment Issue",
    "Order Issue",
    "Refund Issue",
    "Technical Issue"
]

category_matrix = confusion_matrix(
    y_category_test,
    category_predictions,
    labels=category_labels
)

category_matrix_df = pd.DataFrame(
    category_matrix,
    index=category_labels,
    columns=category_labels
)

print("\nCategory Confusion Matrix:")

print(category_matrix_df)


# ==========================================
# 9. PRIORITY MODEL
# ==========================================

priority_vectorizer = TfidfVectorizer()

X_priority_train_vectorized = priority_vectorizer.fit_transform(
    X_priority_train
)

X_priority_test_vectorized = priority_vectorizer.transform(
    X_priority_test
)


priority_model = LogisticRegression(
    max_iter=1000
)

priority_model.fit(
    X_priority_train_vectorized,
    y_priority_train
)


# ==========================================
# 10. PRIORITY PREDICTIONS
# ==========================================

priority_predictions = priority_model.predict(
    X_priority_test_vectorized
)


priority_accuracy = accuracy_score(
    y_priority_test,
    priority_predictions
)

print("\n===================================")
print("PRIORITY MODEL")
print("===================================")

print(
    "Priority Model Accuracy:",
    priority_accuracy
)


# ==========================================
# 11. PRIORITY CLASSIFICATION REPORT
# ==========================================

print("\nPriority Classification Report:")

print(
    classification_report(
        y_priority_test,
        priority_predictions,
        zero_division=0
    )
)


# ==========================================
# 12. PRIORITY CONFUSION MATRIX
# ==========================================

priority_labels = [
    "Low",
    "Medium",
    "High"
]

priority_matrix = confusion_matrix(
    y_priority_test,
    priority_predictions,
    labels=priority_labels
)

priority_matrix_df = pd.DataFrame(
    priority_matrix,
    index=priority_labels,
    columns=priority_labels
)

print("\nPriority Confusion Matrix:")

print(priority_matrix_df)


# ==========================================
# 13. TEST WITH NEW CUSTOMER TICKETS
# ==========================================

new_tickets = [

    "My bank account was charged but my order didn't go through.",

    "I was charged twice for the same purchase.",

    "My refund has not arrived after 30 days.",

    "My order has not arrived for two weeks.",

    "The application crashes when I open it."

]


print("\n===================================")
print("TEST PREDICTIONS")
print("===================================")


for ticket in new_tickets:

    # Convert ticket into TF-IDF features

    category_vector = category_vectorizer.transform(
        [ticket]
    )

    priority_vector = priority_vectorizer.transform(
        [ticket]
    )


    # Predict category

    predicted_category = category_model.predict(
        category_vector
    )[0]


    # Predict priority

    predicted_priority = priority_model.predict(
        priority_vector
    )[0]


    print("\nTicket:")
    print(ticket)

    print(
        "Category:",
        predicted_category
    )

    print(
        "Priority:",
        predicted_priority
    )


# ==========================================
# 14. SAVE CATEGORY MODEL
# ==========================================

joblib.dump(
    category_model,
    "model/category_model.pkl"
)

joblib.dump(
    category_vectorizer,
    "model/category_vectorizer.pkl"
)


# ==========================================
# 15. SAVE PRIORITY MODEL
# ==========================================

joblib.dump(
    priority_model,
    "model/priority_model.pkl"
)

joblib.dump(
    priority_vectorizer,
    "model/priority_vectorizer.pkl"
)


# ==========================================
# 16. FINISHED
# ==========================================

print("\n===================================")
print("MODELS SAVED SUCCESSFULLY!")
print("===================================")