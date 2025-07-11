import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("upi_transactions.xlsx")

# Select features and label
X = df[['Amount', 'User_ID', 'Receiver_ID']]
y = df['Is_Fraud']

# Balance data
sm = SMOTE(random_state=42)
X_resampled, y_resampled = sm.fit_resample(X, y)

# Train model (Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_resampled, y_resampled)

# Streamlit App
st.title("💳 UPI Fraud Detection App")

# Inputs
amount = st.number_input("Enter transaction amount (₹)", min_value=0.0, step=100.0)
user_id = st.number_input("Enter User ID", min_value=0)
receiver_id = st.number_input("Enter Receiver ID", min_value=0)

if st.button("Predict"):
    input_df = pd.DataFrame([[amount, user_id, receiver_id]], columns=['Amount', 'User_ID', 'Receiver_ID'])
    
    # Predict
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    # Show result
    if prediction == 1:
        st.error(f"🚨 This transaction is FRAUD!\n🔍 Confidence: {proba[1]:.2%}")
    else:
        st.success(f"✅ This transaction is NOT fraud.\n🔍 Confidence: {proba[0]:.2%}")

    # Plot probabilities
    st.subheader("📊 Prediction Probabilities")
    fig, ax = plt.subplots()
    ax.bar(['Not Fraud (0)', 'Fraud (1)'], proba, color=['green', 'red'])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")
    ax.set_title("Prediction Confidence")
    st.pyplot(fig)
