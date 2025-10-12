# ...existing code...

# --- Prediction Page ---
st.header("Survival Prediction")

st.subheader("Enter Passenger Information:")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.number_input("Age", min_value=0, max_value=100, value=30)
fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)

if st.button("Predict Survival Probability"):
    # Simple rule-based prediction: females have higher survival probability
    if sex == "female":
        proba = 0.75
    else:
        proba = 0.25
    st.success(f"Predicted Survival Probability (rule-based): {proba:.2%}")