import pickle
import streamlit as st
import requests
import pandas as pd
import base64

# Function to encode a local image as Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return encoded_image

# Function to set a background using a local image
def set_background(image_path):
    encoded_image = get_base64_image(image_path)
    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .custom-title {{
        font-size: 60px;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-top: 30px;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&api_key=0d925d19aefd8a689cd5c52f27ca2e24"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Set background image (local image file)
set_background(r"C:\\Users\\Aman Rai\\Downloads\\app background.jpg")  # Update with your image path

# Styled title
st.markdown('<div class="custom-title">CineMatch</div>', unsafe_allow_html=True)

# Load your data and similarity model
movies = pickle.load(open('movies.pkl', 'rb'))  # Replace with the actual file path
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Replace with the actual file path

# User input and recommendations
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display recommendations in a horizontal layout
    cols = st.columns(len(recommended_movie_names))  # Create columns for each recommendation
    for col, name, poster_url in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="{poster_url}" style="border: 3px solid white; border-radius: 20px; width: 250px; height: 225px;">
                    <h4 style="color: white;">{name}</h4>
                </div>
                """, 
                unsafe_allow_html=True
            )
