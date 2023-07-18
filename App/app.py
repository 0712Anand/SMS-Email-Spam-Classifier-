import streamlit as st 
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transformed_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []

    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Detector")

input_sms = st.text_area("Enter the message Please !")

if st.button('Predict'):

    #preprocess
    transformed_sms = transformed_text(input_sms)

    #vectorize
    vector_input = tfidf.transform([transformed_sms])

    #predict
    result = model.predict(vector_input)

    #display
    if result==1:
        st.header("It is SPAM")
    else:
        st.header(" NOT SPAM")