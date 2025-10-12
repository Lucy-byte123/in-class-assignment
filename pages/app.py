import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os

warnings.filterwarnings('ignore', message="Thread 'MainThread': missing ScriptRunContext!")
sns.set_style("whitegrid")

st.title("Titanic App by Xinzhi Zhang")

# Check if train.csv exists before loading
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