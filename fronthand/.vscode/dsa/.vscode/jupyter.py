import pandas as pd

# Load the Excel file
df = pd.read_excel("upi_transactions.xlsx")  # change name if different

# Show first 5 rows
print(df.head())

# Optional: Check fraud vs non-fraud counts
print(df['Is_Fraud'].value_counts())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Select features and label
X = df[['Amount']]  # We are using just 'Amount' for simplicity now
y = df['Is_Fraud']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
