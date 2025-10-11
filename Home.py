import streamlit as st

# Set page config - must be the first Streamlit command
st.set_page_config(
    page_title="World Cities - Home",
    page_icon="🌍",
    layout="wide"
)

# Main title
st.title('🌍 Welcome to World Cities App')

# Welcome text
st.markdown("""
### Explore Cities Around the World

Welcome! This application allows you to explore and visualize data about major cities across the globe.
Discover population statistics, geographic distributions, and much more!

#### Getting Started:
👈 Use the sidebar to navigate to different pages of the application.

#### Features:
- 🗺️ **Interactive Map**: View cities on an interactive world map
- 📊 **Data Visualization**: Analyze population distribution by country
- 🔍 **Advanced Filtering**: Filter cities by population, capital status, and country
- 📈 **Population Statistics**: View detailed city information and statistics

#### How to Navigate:
Click on the pages in the sidebar to explore different sections of the application.
""")

# Add a visual separator
st.markdown("---")

# Information box with navigation hint
st.info("👈 **Ready to explore?** Use the sidebar navigation to visit the **app** page and start exploring world cities!")

# Optional: Add a button as an alternative navigation method
st.markdown("""
### Quick Links
Navigate to the app page using the sidebar on the left to start exploring the world cities data.
""")
