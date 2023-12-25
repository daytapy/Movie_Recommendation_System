import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=1ab7b0577d97ea1312d53d75ccb5a262&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def rekom(film):
    mv_idx = df[df['title']==film].index[0]
    kemiripan = sm[mv_idx]
    list_rekom = sorted(list(enumerate(kemiripan)),reverse=True,key=lambda x:x[1])[1:6]

    rekom_poster = []
    rekom_film = []
    for i in list_rekom:
        movie_id = df.iloc[i[0]].movie_id
        rekom_poster.append(fetch_poster(movie_id))
        rekom_film.append((df.iloc[i[0]].title))
    return rekom_film, rekom_poster

with open('filmDict.pkl', 'rb') as file:
    data = pickle.load(file)
df = pd.DataFrame(data)

with open('smlr.pkl', 'rb') as file:
    sm = pickle.load(file)

st.toast('😴😴😴😴😴')
st.title('Movie Recommender System 📽️')
st.info('Sistem Rekomendasi Film adalah aplikasi atau sistem yang dirancang untuk memberikan rekomendasi film kepada pengguna berdasarkan preferensi mereka atau perilaku penonton sebelumnya. Tujuan utamanya adalah meningkatkan pengalaman pengguna dengan menyajikan konten yang paling relevan dan sesuai dengan minat mereka, sehingga meningkatkan kepuasan penonton dan dapat meningkatkan retensi pengguna.')
pilih = st.selectbox('Pilih film yang kamu suka',df['title'].values)

if st.button('Rekomendasi'):
    rekom_film, rekom_poster = rekom(pilih)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(rekom_film[0])
        st.image(rekom_poster[0])
    with col2:
        st.text(rekom_film[1])
        st.image(rekom_poster[1])
    with col3:
        st.text(rekom_film[2])
        st.image(rekom_poster[2])
    with col4:
        st.text(rekom_film[3])
        st.image(rekom_poster[3])
    with col5:
        st.text(rekom_film[4])
        st.image(rekom_poster[4])

st.caption("Info lebih lanjut ada di https://github.com/daytapy, selamat belajar 🚀")
    