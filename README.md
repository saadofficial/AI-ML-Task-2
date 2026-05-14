# 📈 Task 2 - Stock Price Prediction Using Machine Learning

## 👨‍💻 Author
**Saad Khanzada**  
AI/ML Remote Internship

---

# 📌 Project Overview

This project focuses on predicting future stock closing prices using Machine Learning techniques. Historical stock market data was collected from Yahoo Finance using the `yfinance` Python library, and a Linear Regression model was trained to predict stock closing prices based on different stock market features.

The project demonstrates the complete Machine Learning workflow including:

- Data collection
- Data preprocessing
- Feature selection
- Model training
- Prediction
- Performance evaluation
- Data visualization

---

# 🎯 Objective

The main objective of this task is to:

- Learn how to work with real-world financial datasets
- Understand regression-based Machine Learning models
- Predict stock closing prices using historical data
- Visualize prediction performance using graphs

---

# 📊 Dataset Information

## Dataset Source
The dataset was retrieved directly from Yahoo Finance using the `yfinance` API.

### Stock Selected
- **Apple Inc. (AAPL)**

---

## Dataset Features

The dataset contains historical stock market information such as:

| Feature | Description |
|---|---|
| Open | Stock price at market opening |
| High | Highest stock price during the day |
| Low | Lowest stock price during the day |
| Close | Final stock price at market closing |
| Volume | Number of shares traded |

---

# 🛠 Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data handling and analysis |
| yFinance | Fetching stock market data |
| Scikit-learn | Machine Learning model training |
| Matplotlib | Data visualization |

---

# 🧠 Machine Learning Concept Used

## Linear Regression

Linear Regression is a supervised Machine Learning algorithm used for predicting numerical values.

In this project, the model learns relationships between stock market features and predicts the closing stock price.

### Input Features
- Open Price
- High Price
- Low Price
- Volume

### Target Variable
- Close Price

---

# 🔄 Project Workflow

The project was completed in the following steps:

---

## 1️⃣ Data Collection

Historical stock market data was downloaded using the `yfinance` library.

```python
stock_data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")
```

This downloaded one year of Apple stock data.

---

## 2️⃣ Data Inspection

The dataset was inspected using:

- `.head()`
- `.shape`
- `.info()`

This helped in understanding:
- Dataset structure
- Column names
- Data types
- Missing values

---

## 3️⃣ Feature Selection

The following features were selected as input variables:

```python
X = stock_data[["Open", "High", "Low", "Volume"]]
```

The target variable selected was:

```python
y = stock_data["Close"]
```

---

## 4️⃣ Data Splitting

The dataset was divided into:
- Training Data (80%)
- Testing Data (20%)

```python
train_test_split()
```

### Purpose
- Training data teaches the model
- Testing data evaluates model performance

---

## 5️⃣ Model Training

A Linear Regression model was created and trained using:

```python
model.fit(X_train, y_train)
```

The model learned patterns from historical stock market data.

---

## 6️⃣ Prediction

Predictions were generated using:

```python
predictions = model.predict(X_test)
```

The model predicted stock closing prices for unseen data.

---

## 7️⃣ Model Evaluation

The model performance was checked using:

### Mean Squared Error (MSE)

```python
mean_squared_error()
```

### Purpose
Measures prediction error between:
- Actual prices
- Predicted prices

Lower error values indicate better predictions.

---

## 8️⃣ Data Visualization

A graph was created to compare:
- Actual stock prices
- Predicted stock prices

### Visualization Used
- Line Plot

This helped in visually understanding the model performance.

---

# 📉 Graph Output

The graph displays two lines:

| Line | Description |
|---|---|
| Actual Prices | Real stock closing prices |
| Predicted Prices | AI predicted prices |

If both lines are close to each other, it indicates good prediction performance.

---

# 📚 Skills Learned

Through this project, the following skills were learned:

- Working with APIs
- Handling real-world datasets
- Data preprocessing
- Regression modeling
- Machine Learning workflow
- Data visualization
- Model evaluation

---

# 🧾 Key Concepts Explained

## 🔹 Machine Learning
A field of Artificial Intelligence where systems learn patterns from data.

---

## 🔹 Regression
A Machine Learning technique used to predict numerical values.

Examples:
- House prices
- Temperature
- Stock prices

---

## 🔹 Features
Input variables used for prediction.

Examples:
- Open Price
- High Price

---

## 🔹 Target Variable
The output value the model predicts.

Example:
- Close Price

---

## 🔹 Training
The process where the model learns from historical data.

---

## 🔹 Prediction
Using learned patterns to estimate future values.

---

# ✅ Results

The Linear Regression model successfully predicted stock closing prices using historical market data.

The comparison graph between actual and predicted prices showed that the model was able to capture stock price trends effectively.

---

# 🚀 Future Improvements

The project can be improved by:

- Using advanced Machine Learning models
- Using more historical data
- Adding technical indicators
- Implementing Deep Learning models
- Predicting multiple future days

---

# 📂 Project Structure

```plaintext
Task-2-Stock-Prediction/
│
├── Task2.py
├── README.md
├── stock_prediction_graph.png
```

---

# ▶️ How to Run the Project

## Step 1 — Install Required Libraries

```bash
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install yfinance
```

---

## Step 2 — Run the Python File

```bash
python Task2.py
```

---

# 📌 Conclusion

This project provided practical experience in Machine Learning and stock market prediction. It demonstrated how historical financial data can be used to train predictive models and visualize prediction results effectively.

The project also strengthened understanding of:
- Data analysis
- Regression models
- Prediction systems
- Python libraries used in AI/ML

---

# 🙌 Acknowledgement

This project was completed as part of an AI/ML Remote Internship task to gain practical experience in data analysis and Machine Learning.
