import streamlit as st
from PIL import Image

# Title for the section
st.title('Music Recommendation System Visualization')

# Create two columns for the images
col1, col2 = st.columns(2)

# Most Popular Tracks
with col1:
    st.header('Most Popular Tracks')
    image1 = Image.open('images/popular_tracks.png')
    st.image(image1)

# Correlation Map

with col2:
    st.header('Correlation Map')
    image4 = Image.open('images/corr.png')
    st.image(image4)

# Create another two columns for the next row of images
col3, col4 = st.columns(2)

# No of tracks added 
with col3:
    
    st.header('No of Tracks Added')
    image2 = Image.open('images/track_added.png')
    st.image(image2)

# Audio Characteristics
with col4:
    st.header('Audio Characteristics')
    image3 = Image.open('images/audioc.png')
    st.image(image3)

    # Add some description or interactivity to each image
if st.checkbox("Show Details"):
    st.write("""
    ### Most Popular Tracks
    This image shows the distribution of popularity among tracks in the dataset.
    
    ### Correlation Map
    The correlation map displays the relationship between different audio features of tracks.
    
    ### No of Tracks Added
    This visualization indicates the number of tracks added over time.
    
    ### Audio Characteristics
    The audio characteristics image illustrates various attributes such as danceability, energy, etc.
    """)
