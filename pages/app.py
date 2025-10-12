import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore', message="Thread 'MainThread': missing ScriptRunContext!")
sns.set_style("whitegrid")

# Set the title of the app
st.title("Titanic App by Xinzhi Zhang")

# Load the Titanic dataset
try:
    df = pd.read_csv('train.csv')
    # Display the entire DataFrame in the Streamlit app
    st.subheader("Titanic DataFrame")
    st.dataframe(df)

    # Create subplots for the boxplots
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

except FileNotFoundError:
    st.error("Error: The 'train.csv' file was not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.exception(e)