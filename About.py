import streamlit as st

# Header and Introduction
st.title("🎵 Music Recommendation System 🎵")
st.write("Welcome to the Music Recommendation System Dashboard! 🎶 Use the sidebar to navigate. 🚀")

# About Page
st.title("About ℹ️")
st.image("abt.jpg", use_column_width=True)
st.markdown("---")

st.write("""
This dashboard is designed to help you explore and discover music based on various attributes such as mood, danceability, acousticness, and energy. 

### Key Features:
- **Interactive Visualizations:** Explore music attributes through interactive visualizations such as scatter plots and 3D charts. 📊
- **Filtering:** Use sidebar filters to refine your music search based on mood, danceability, acousticness, and energy. 🔍
- **Data Exploration:** Dive deeper into the dataset with summary statistics. 📈

### Dataset Information:
The dataset used in this dashboard contains information about various songs, including their attributes like danceability, energy, acousticness, popularity, and mood. 📋

### How to Use:
1. Use the sidebar to select filters based on your preferences.
2. Choose visualizations from the sidebar to explore different aspects of the data.
3. Enjoy exploring and discovering new music! 🎧🎶

Feel free to explore and find your favorite songs! 🎉
""")

# Additional Information
st.markdown("---")  # Add another horizontal line for separation
st.subheader("Additional Information ℹ️")
st.write("""
- **Dataset Source:** No specific source provided. 🤷‍♂️
- **Created By:** [Likitha Yadav G] 🧑‍💻
- **Contact Information:** [likitha@12345.gmail.com] ✉️
""")
