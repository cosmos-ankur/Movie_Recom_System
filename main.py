import streamlit as st
import pickle
import pandas as pd

def recomend(movie):
    #sort to find closese distances but also require to preserve index so we will use enumerate
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender')
selected_movie_name = st.selectbox(
    'Choose your Movie',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recomend(selected_movie_name)
    for i in recommendations:
        st.write(i)