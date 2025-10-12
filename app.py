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
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Boxplot 1: Fare distribution for Pclass = 1
sns.boxplot(x="Pclass", y="Fare", data=df[df["Pclass"] == 1], ax=axes[0])
axes[0].set_title('Fare Distribution for Pclass 1')
axes[0].set_xlabel('Passenger Class (Pclass)')
axes[0].set_ylabel('Fare')

# Boxplot 2: Fare distribution for Pclass = 2
sns.boxplot(x="Pclass", y="Fare", data=df[df["Pclass"] == 2], ax=axes[1])
axes[1].set_title('Fare Distribution for Pclass 2')
axes[1].set_xlabel('Passenger Class (Pclass)')
axes[1].set_ylabel('Fare')

# Boxplot 3: Fare distribution for Pclass = 3
sns.boxplot(x="Pclass", y="Fare", data=df[df["Pclass"] == 3], ax=axes[2])
axes[2].set_title('Fare Distribution for Pclass 3')
axes[2].set_xlabel('Passenger Class (Pclass)')
axes[2].set_ylabel('Fare')

# Adjust layout to avoid overlap
plt.tight_layout()

# Display the plot in the Streamlit app
st.pyplot(fig)
