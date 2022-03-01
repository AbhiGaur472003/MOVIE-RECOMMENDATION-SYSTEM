import pickle
import streamlit as st
import requests
import pandas as pd

# fetch the poster of movie when the movie_id is given
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster = data['poster_path']
    path = "https://image.tmdb.org/t/p/w500/" + poster
    return path

# fetch the index of movie when title is given
def Idx(movie):
    for i in range(len(movies)):
        if movies['title'][i]==movie:
            return i
#     return 0

# fetch the index of movie in particular column of similarity
def fetchmovieIdx(obj,n):
    c=0
    for i in similarity[n]:
        if i==obj:
            break
        c+=1
    # st.text(c)
    return c

def RecommendMovie(movie):
    #fetch the index of movie
    idx=Idx(movie)

    List=sorted(similarity[idx],reverse=True)
    List=List[1:11]
    recommended_names = []
    recommended_posters = []
    for i in List:
        c=fetchmovieIdx(i,idx)
        movie_id=movies['movie_id'][c]
        # st.text(movie_id)
        recommended_posters.append(fetch_poster(movie_id))
        recommended_names.append(movies['title'][c])

    return recommended_names ,recommended_posters

# Use to set Header of our application
st.header('Movie Recommender System')

# Loads the file from current location
movies = pickle.load(open('movie_list.csv','rb'))
similarity = pickle.load(open('similarity.csv','rb'))

# Create a list or array which contains all the titles of movies
list1 = movies['title'].values

# Create a box which contains movies list and we have to select any one
selected_movie = st.selectbox("Select a movie for recommendation",list1)

# st.text(movies)

if st.button('Display Recommended movies'):
    names,posters = RecommendMovie(selected_movie)

    # Creates 5 columns of equal sizes(height and width)
    col1,col2,col3,col4,col5= st.columns(5)
    col11,col22,col33,col44,col55=st.columns(5)
    
    with col1:
        st.image(posters[0])
        st.text(names[0])
    with col2:
        st.image(posters[1])
        st.text(names[1])
    with col3:
        st.image(posters[2])
        st.text(names[2])
    with col4:
        st.image(posters[3])
        st.text(names[3])
    with col5:
        st.image(posters[4])
        st.text(names[4])

    with col11:
        st.image(posters[5])
        st.text(names[5])
    with col22:
        st.image(posters[6])
        st.text(names[6])
    with col33:
        st.image(posters[7])
        st.text(names[7])
    with col44:
        st.image(posters[8])
        st.text(names[8])
    with col55:
        st.image(posters[9])
        st.text(names[9])
