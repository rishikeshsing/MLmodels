import streamlit as st
from textblob import TextBlob

st.sidebar.title("About us")
st.sidebar.text("""It's just a simple sentiment analysis
project based on textblob
""")

st.sidebar.title("Contact us")
st.sidebar.text("""https://www.linkedin.com/in/rishikeshsing/
rishikeshsin786@gmail.com
Noida, UP 201301, India
""")

st.title("Sentiment Analysis Project")

text=st.text_input("**enter text**")
btn=st.button("predict")

if btn:
    blob=TextBlob(text)
    sen=blob.sentiment[0]
    if sen<0:
        st.error("Negative Sentiment")
        st.image("neg.jpg")
    elif sen>0:
        st.success("Positive Sentiment")
        st.image("pos.jpg")
    else:
        st.warning("Neutral Sentiment")
        st.image("neu.jpg")


