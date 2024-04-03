import streamlit as st
import os

# Title for the app
st.title('Add Your Favorite Songs')

# Create a text input for users to add songs
song_name = st.text_input('Enter the name of your favorite song:', '')

# Button to add the song
if st.button('Add Song'):
    if song_name:
        with open("favorite_songs.txt", "a") as f:
            f.write(song_name + "\n")
        st.success(f'🎵 "{song_name}" has been added!')
    else:
        st.warning('⚠️ Please enter a song name before adding.')

# Display all added songs
st.subheader('List of Favorite Songs:')
# Read the list of favorite songs from the file
if os.path.exists("favorite_songs.txt"):
    with open("favorite_songs.txt", "r") as f:
        favorite_songs = f.readlines()
        for song in favorite_songs:
            st.write(f'🎶 {song.strip()}')
else:
    st.write("No favorite songs added yet.")
