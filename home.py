import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore', message="Thread 'MainThread': missing ScriptRunContext!")
sns.set_style("whitegrid")

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Welcome to the Titanic Data App!")
st.write(
    """
    This is the Home page.  
    Explore Titanic passenger data and predictions usinhome.pyg our interactive app.
    """
)

if st.button("Go to Titanic App"):
    st.experimental_redirect("app.py")


