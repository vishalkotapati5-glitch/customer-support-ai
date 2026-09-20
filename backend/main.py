from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

# Create FastAPI application
app = FastAPI(title="Customer Support AI")

# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained category model
category_model = joblib.load("model/category_model.pkl")
category_vectorizer = joblib.load("model/category_vectorizer.pkl")

# Load trained priority model
priority_model = joblib.load("model/priority_model.pkl")
priority_vectorizer = joblib.load("model/priority_vectorizer.pkl")


# Request data format
class TicketRequest(BaseModel):
    message: str


# Home route
@app.get("/")
def home():
    return {
        "message": "Customer Support AI API is running"
    }


# Prediction route
@app.post("/predict")
def predict(ticket: TicketRequest):

    # Convert customer message into numerical features
    category_input = category_vectorizer.transform(
        [ticket.message]
    )

    priority_input = priority_vectorizer.transform(
        [ticket.message]
    )

    # Predict category
    category = category_model.predict(
        category_input
    )[0]

    # Predict priority
    priority = priority_model.predict(
        priority_input
    )[0]

    # Return result
    return {
        "message": ticket.message,
        "category": category,
        "priority": priority
    }