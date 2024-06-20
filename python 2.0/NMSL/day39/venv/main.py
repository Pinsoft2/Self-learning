import streamlit as st
import plotly.express as px
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import os


st.title("Diary Tone")
st.subheader("Positivity")


articles = []
names = []
diary_overall = {}
diary_neg_overall = {}
#get data
#create a dictionary for later sorting

analyzer = SentimentIntensityAnalyzer()

for filename in sorted(os.listdir("diary")):
    with open(f"diary/{filename}") as file:
        article = file.read()
        articles.append(article)
        name = os.path.splitext(filename)[0]
        names.append(name)
        pos_scores=[]
        for diary in articles:
            score = analyzer.polarity_scores(diary)['pos']
            neg_score = analyzer.polarity_scores(diary)['neg']
            pos_scores.append(score)
            diary_neg_overall.update({name:neg_score})
            diary_overall.update({name:score})
#store pos score to each dairy

myKeys = list(diary_overall.keys())
myKeys.sort()
sorted_dict = {i: diary_overall[i] for i in myKeys}
sorted_dict_neg = {i: diary_neg_overall[i] for i in myKeys}

figure = px.line(x=sorted_dict.keys(), y=sorted_dict.values(), labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)
#plot data

st.subheader("Negativity")

figure_neg = px.line(x=sorted_dict_neg.keys(), y=sorted_dict_neg.values(), labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_neg)