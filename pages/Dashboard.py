import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Read the CSV data
data = pd.read_csv('data_moods.csv')

# Set the page configuration
st.set_page_config(page_title="Music Dashboard", layout="wide")

# Add a title
st.title("Music Dashboard")

# Create a sidebar for filters
st.sidebar.title("Filters")

# Multiselect for selecting moods
selected_moods = st.sidebar.multiselect("Select Moods", data['mood'].unique(), default=data['mood'].unique())

# Slider for danceability
selected_danceability = st.sidebar.slider("Select Danceability Range", min_value=0.0, max_value=1.0, value=(0.0, 1.0))

# Slider for energy
selected_energy = st.sidebar.slider("Select Energy Range", min_value=0.0, max_value=1.0, value=(0.0, 1.0))

# Filter the data based on selected filters
filtered_data = data[(data['mood'].isin(selected_moods)) &
                     (data['danceability'] >= selected_danceability[0]) &
                     (data['danceability'] <= selected_danceability[1]) &
                     (data['energy'] >= selected_energy[0]) &
                     (data['energy'] <= selected_energy[1])]

# Create metrics for Total Length and Average Popularity
col1, col2 = st.columns(2)
with col1:
    total_length = filtered_data['length'].sum()
    st.metric("Total Length (ms)", f"{total_length:,.0f}")
with col2:
    mean_popularity = filtered_data['popularity'].mean().round(2)
    st.metric("Average Popularity", f"{mean_popularity}")

# Create metrics for Average Danceability and Average Energy
col3, col4 = st.columns(2)
with col3:
    mean_danceability = (filtered_data['danceability'].mean() * 100).round(2)
    st.metric("Average Danceability", f"{mean_danceability} %")
with col4:
    mean_energy = (filtered_data['energy'].mean() * 100).round(2)
    st.metric("Average Energy", f"{mean_energy} %")

# Create a container to hold the plots
container = st.container()

# Create a 3D scatter plot for danceability, energy, and loudness
with container:
    row1, row2 = st.columns(2)
    with row1:
        with st.expander("3D Scatter Plot"):
            fig = px.scatter_3d(filtered_data, x='danceability', y='energy', z='loudness',
                                color='mood', hover_name='name',
                                title='Danceability, Energy, and Loudness by Mood')
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with st.expander("Length and Popularity"):
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['length'], mode='lines', name='Length'))
            fig.add_trace(go.Scatter(x=filtered_data.index, y=filtered_data['popularity'], mode='lines', name='Popularity'))
            fig.update_layout(title='Length and Popularity', xaxis_title='Index', yaxis_title='Value')
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    with row2:
        with st.expander("Mood Counts"):
            fig = px.sunburst(filtered_data, path=['mood'], values='length',
                              title='Mood Counts by Length')
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with st.expander("Artists and Albums"):
            fig = px.sunburst(filtered_data, path=['artist', 'album'], values='length',
                              title='Artists and Albums by Length')
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# Display images
st.subheader("Images")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("newplot.png", caption="Image 1", use_column_width=True)
with col2:
    st.image("newplot (1).png", caption="Image 2", use_column_width=True)
with col3:
    st.image("newplot (2).png", caption="Image 3", use_column_width=True)

# Add video elements
col4, col5 = st.columns(2)
with col4:
    st.video("https://www.youtube.com/watch?v=PFTRVXy3974") 
with col5:
    st.video("https://www.youtube.com/watch?v=z2ZuYWnUhVw")
