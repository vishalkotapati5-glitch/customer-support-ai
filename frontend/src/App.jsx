import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const classifyTicket = async () => {
    if (!message.trim()) {
      setError("Please enter a customer message.");
      return;
    }

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: message,
          }),
        }
      );

      if (!response.ok) {
        throw new Error("API request failed");
      }

      const data = await response.json();

      setResult(data);
    } catch (error) {
      console.error("Error:", error);

      setError(
        "Could not connect to the AI backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>Customer Support AI</h1>

        <p className="subtitle">
          AI-powered customer ticket classification
        </p>

        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Enter a customer support message..."
        />

        <button
          onClick={classifyTicket}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Ticket"}
        </button>

        {error && (
          <div className="error">
            {error}
          </div>
        )}

        {result && (
          <div className="result">
            <h2>Prediction Result</h2>

            <p>
              <strong>Category:</strong>{" "}
              {result.category}
            </p>

            <p>
              <strong>Priority:</strong>{" "}
              {result.priority}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;