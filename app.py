import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore', message="Thread 'MainThread': missing ScriptRunContext!")
sns.set_style("whitegrid")


# Apply seaborn style for better aesthetics
sns.set(style="whitegrid")

# Set the title of the app
st.title("Titanic App by Xinzhi Zhang")

# Load the Titanic dataset
try:
    try:
        df = pd.read_csv('titanic.csv')
    except:
        df = pd.read_csv('titanic.csv')
# Load and display the dataframe
    st.subheader("Titanic DataFrame")

# Display the entire DataFrame in the Streamlit app
    st.dataframe(df)

# Create subplots for the boxplots
   for i, pclass in enumerate([1, 2, 3]):
         class_data = df[df['Pclass'] == pclass]

         sns.boxplot(y=class_data['Fare'], ax=axes[i])

         axes[i].set_title(f'Pclass = {pclass}')
           axes[i].set_xlabel('Passenger Class')
           axes[i].set_ylabel('Fare')
    plt.tight_layout()
    st.subheader("Fare Distribution by Passenger Class")
    plt.tight_layout()        