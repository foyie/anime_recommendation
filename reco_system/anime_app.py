
import streamlit as st
import pickle
import pandas as pd
import requests

anime_dict=pickle.load(open('anime_dict.pkl','rb'))
anime_df=pd.DataFrame(anime_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(anime_name):
    url= (anime_df.loc[anime_df['title'] == anime_name, 'img_url'].item())or(anime_df.loc[anime_df['title2'] == anime_name, 'img_url'].item())
    # data=data.json()
    return url

def recommend(anime_name):
    anime_index=anime_df[anime_df['title']==anime_name].index[0]
    distances=similarity[anime_index]
    anime_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_anime=[]
    recommended_anime_poster=[]
    for i in anime_list:
        # anime_id=anime_df.iloc[i[0]].movie_id
        recommended_anime.append(anime_df.iloc[i[0]].title)
        #fetching poster
        recommended_anime_poster.append(fetch_poster(anime_df.iloc[i[0]].title))
    return recommended_anime,recommended_anime_poster

st.title('Movie Recommender System')

selected_anime_name = st.selectbox(
'Please enter the anime_df name',
(anime_df['title'].values))

if st.button('Recommend'):
    names,posters=recommend(selected_anime_name)

    #recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)
    
   
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
