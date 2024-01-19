import nltk

# nltk.download("punkt")
# nltk.download("stopwords")

import pathlib

pathlib.Path().resolve()
import pandas as pd

ms = pd.read_csv("musicFinder_2.csv")

ms = ms[ms["release_date"] >= 2000]
ms = ms[["artist_name", "track_name", "release_date", "genre", "lyrics", "topic"]]

import re
import numpy as np
import contractions

stop_words = nltk.corpus.stopwords.words("english")


def normalize_document(doc):
    # lower case and remove special characters\whitespaces
    doc = re.sub(r"[^a-zA-Z0-9\s]", "", doc, re.I | re.A)
    doc = doc.lower()
    doc = doc.strip()
    doc = contractions.fix(doc)
    # tokenize document
    tokens = nltk.word_tokenize(doc)
    # filter stopwords out of document
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # re-create document from filtered tokens
    doc = " ".join(filtered_tokens)
    return doc


normalize_corpus = np.vectorize(normalize_document)

norm_corpus = normalize_corpus(list(ms["lyrics"]))

from sklearn.feature_extraction.text import TfidfVectorizer

tf = TfidfVectorizer(ngram_range=(1, 2), min_df=2)
tfidf_matrix = tf.fit_transform(norm_corpus)

from sklearn.metrics.pairwise import cosine_similarity

doc_sim = cosine_similarity(tfidf_matrix)
doc_sim_df = pd.DataFrame(doc_sim)

song_list = ms["track_name"].values


def music_finder(song_name, songs=song_list, doc_sim=doc_sim_df):
    song_id = np.where(songs == song_name)[0][0]
    song_similarities = doc_sim.iloc[song_id].values
    similar_song_id = np.argsort(-song_similarities)[1:6]
    similar_song = songs[similar_song_id]
    return similar_song


# ============================================================================================================================
import streamlit as st

st.set_page_config(page_title="Music Finder", page_icon=":🎵:")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
background-image: url("https://images5.alphacoders.com/923/923417.jpg"); /* Main Background */
background-size: cover;
}

.st-emotion-cache-1avcm0n {
background-color: #ffffff60; /* Header */
}

.st-emotion-cache-13k62yr{
margin: 0 -10% 0 -10%; /* Container */
}

.st-emotion-cache-zt5igj {
text-align: center; /* Title */
color: black;
}

.st-emotion-cache-nahz7x {
color: black; /* Subtitle */
margin-top: -4%;
text-align: center;
}

.st-emotion-cache-nahz7x a{
color: black; /* Hyperlink */
}

.st-emotion-cache-q8sbsg{
color:black; /* Markdown label */
}

.st-b7 {
background-color: #ffffff80; /* Input Form */
}

.st-bb {
color: black;
}

.st-emotion-cache-1xw8zd0 {
border: 2px solid rgb(250, 250, 250);
}

[data-testid="stMarkdownContainer"] > .st-emotion-cache-nahz7x {
text-align: left;
}

code {
color: black;
background: none
}

</style>
"""

url = "https://docs.google.com/spreadsheets/d/1jBNEBqY-sd-2XIjveztsXKUuQuHymbnT/edit?usp=drive_link&ouid=117640975622875564932&rtpof=true&sd=true"

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Music Finder")
st.write("_Pencarian musik dari tahun 2000 hingga 2019_")
st.write("_[Klik untuk melihat daftar lagu](%s)_" % url)
st.write("")

inputSong = st.text_input("Masukan judul lagu...")
if st.button("Cari"):
    result = music_finder(song_name=inputSong, songs=song_list, doc_sim=doc_sim_df)
    detail = ms.loc[ms["track_name"].isin(result)]
    # sorted_detail = detail.sort_values(by="track_name")

    st.subheader("Hasil rekomendasi :")
    for index, row in detail.iterrows():
        artist_name = row["artist_name"]
        track_name = row["track_name"]
        release_date = row["release_date"]
        genre = row["genre"]
        topic = row["topic"]

        container = st.container(border=True)
        container.subheader(track_name)
        container.write(artist_name)
        container.write(release_date)
        container.write(genre)
        container.write(topic)
