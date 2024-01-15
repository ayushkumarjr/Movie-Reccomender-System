import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0349f98abdafdc1d16363d54e6608285'
    response = requests.get(url)

    data = response.json()
    return 'https://image.tmdb.org/t/p/w185/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API

        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox('You are Watching',movies['title'].values)

if st.button('Recommend'):
    recommended_movies_names,recommend_movie_posters=recommend(selected_movie_name)
    st.header(recommended_movies_names[0])
    st.image(recommend_movie_posters[0])

    st.header(recommended_movies_names[1])
    st.image(recommend_movie_posters[1])

    st.header(recommended_movies_names[2])
    st.image(recommend_movie_posters[2])

    st.header(recommended_movies_names[3])
    st.image(recommend_movie_posters[3])

    st.header(recommended_movies_names[4])
    st.image(recommend_movie_posters[4])