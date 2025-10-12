import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os
import pickle

warnings.filterwarnings('ignore', message="Thread 'MainThread': missing ScriptRunContext!")
sns.set_style("whitegrid")

st.set_page_config(page_title="Titanic App by Xinzhi Zhang", page_icon="🚢")

st.title("Titanic App by Xinzhi Zhang")

# --- Data Analysis Page ---
st.header("Data Analysis")
csv_path = 'train.csv'
if not os.path.exists(csv_path):
    st.error(f"Error: The '{csv_path}' file was not found in the current directory ({os.getcwd()}). Please check the file path and make sure the file exists.")
else:
    df = pd.read_csv(csv_path)
    st.subheader("Titanic DataFrame")
    st.dataframe(df)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for i, pclass in enumerate([1, 2, 3]):
        class_data = df[df['Pclass'] == pclass]
        sns.boxplot(y=class_data['Fare'], ax=axes[i])
        axes[i].set_title(f'Pclass = {pclass}')
        axes[i].set_xlabel('Passenger Class')
        axes[i].set_ylabel('Fare')
    plt.tight_layout()
    st.subheader("Fare Distribution by Passenger Class")
    st.pyplot(fig)

# --- Prediction Page ---
st.header("Survival Prediction")

model_path = "titanic_model.pkl"
if not os.path.exists(model_path):
    st.error(f"Error: The '{model_path}' file was not found. Please train and save your model as 'titanic_model.pkl'.")
else:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    st.subheader("Enter Passenger Information:")

    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0)

    # Encode inputs
    sex_encoded = 1 if sex == "male" else 0
    input_df = pd.DataFrame([[pclass, sex_encoded, age, fare]], columns=["Pclass", "Sex", "Age", "Fare"])

    if st.button("Predict Survival Probability"):
        proba = model.predict_proba(input_df)[0][1]
        st.success(f"Predicted Survival Probability: {proba:.2%}")