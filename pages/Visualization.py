import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
def load_data():
    return pd.read_csv("data_moods.csv")

data = load_data()

# Sidebar Filters
st.sidebar.title("Filters")
selected_moods = st.sidebar.multiselect("Select Moods", data['mood'].unique(), default=data['mood'].unique())
selected_danceability = st.sidebar.slider("Danceability", min_value=0.0, max_value=1.0, value=(0.0, 1.0), key="danceability_slider")
selected_acousticness = st.sidebar.slider("Acousticness", min_value=0.0, max_value=1.0, value=(0.0, 1.0), key="acousticness_slider")
selected_energy = st.sidebar.slider("Energy", min_value=0.0, max_value=1.0, value=(0.0, 1.0), key="energy_slider")

# Filter the data
filtered_data = data[(data['mood'].isin(selected_moods)) & 
                     (data['danceability'] >= selected_danceability[0]) &
                     (data['danceability'] <= selected_danceability[1]) &
                     (data['acousticness'] >= selected_acousticness[0]) &
                     (data['acousticness'] <= selected_acousticness[1]) &
                     (data['energy'] >= selected_energy[0]) &
                     (data['energy'] <= selected_energy[1])]

# Display Filtered Songs
st.subheader("Filtered Songs")
st.write(filtered_data)

# Data Exploration Tools
st.subheader("Data Exploration Tools")

# Summary Statistics
if st.checkbox("Summary Statistics"):
    st.write(filtered_data.describe())

# Sidebar for choosing visualization
st.sidebar.title("Visualizations")
visualization_choice = st.sidebar.radio("Select Visualization", ["Danceability vs Energy vs Acousticness", "Danceability vs Acousticness vs Energy", "Danceability vs Popularity vs Energy"])  # Unique key

# Selected visualization
if visualization_choice == "Danceability vs Energy vs Acousticness":
    st.subheader("Danceability vs Energy vs Acousticness")
    fig = px.scatter_3d(filtered_data, x='danceability', y='energy', z='acousticness', color='mood', title='Danceability vs Energy vs Acousticness')
    st.plotly_chart(fig)
elif visualization_choice == "Danceability vs Acousticness vs Energy":
    st.subheader("Danceability vs Acousticness vs Energy")
    fig = px.scatter_3d(filtered_data, x='danceability', y='acousticness', z='energy', color='mood', title='Danceability vs Acousticness vs Energy')
    st.plotly_chart(fig)
elif visualization_choice == "Danceability vs Popularity vs Energy":
    st.subheader("Danceability vs Popularity vs Energy")
    fig = px.scatter_3d(filtered_data, x='danceability', y='popularity', z='energy', color='mood', title='Danceability vs Popularity vs Energy')
    st.plotly_chart(fig)
