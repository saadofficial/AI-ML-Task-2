import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Download stock data
stock_data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

# Show first rows
print(stock_data.head())

# Features
X = stock_data[["Open", "High", "Low", "Volume"]]

# Target
y = stock_data["Close"].squeeze()

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test).flatten()

# Compare actual vs predicted
comparison = pd.DataFrame({
    "Actual Price": y_test.to_numpy(),
    "Predicted Price": predictions
})

print(comparison.head())

# Error checking
mse = mean_squared_error(y_test, predictions)

print("\nMean Squared Error:", mse)

# Plot graph
plt.figure(figsize=(10,6))

plt.plot(y_test.to_numpy(), label="Actual Prices")
plt.plot(predictions, label="Predicted Prices")

plt.title("Actual vs Predicted Stock Prices")
plt.xlabel("Days")
plt.ylabel("Stock Price")

plt.legend()

plt.show()