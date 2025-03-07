import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS

# Streamlit App Title
st.title("📊 Instagram Reach Analysis Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload Instagram Data (CSV)", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file, encoding='latin1')
    st.success("File uploaded successfully!")
    
    # Display Dataset Overview
    st.subheader("📌 Dataset Overview")
    st.write(data.head())
    
    # Handling Missing Values
    st.subheader("📌 Missing Values")
    st.write(data.isnull().sum())
    data.dropna(inplace=True)


    
    st.subheader("📌 Data Information")

# Convert problematic data types to strings to avoid Arrow serialization issues
    buffer = pd.DataFrame(data.dtypes.astype(str), columns=['Data Type'])
    st.write(buffer)
    
    # Histogram - Impressions from Home
    st.subheader("📊 Distribution of Impressions From Home")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data['From Home'], kde=True, ax=ax)
    st.pyplot(fig)
    
    # Pie Chart - Impressions Sources
    st.subheader("📊 Impressions on Instagram Posts From Various Sources")
    labels = ['From Home', 'From Hashtags', 'From Explore', 'Other']
    values = [data['From Home'].sum(), data['From Hashtags'].sum(),
              data['From Explore'].sum(), data['From Other'].sum()]
    fig = px.pie(values=values, names=labels, title='Impressions Distribution', hole=0.5)
    st.plotly_chart(fig)
    
    # WordCloud - Captions
    st.subheader("📌 Most Used Words in Captions")
    text = " ".join(i for i in data.Caption.dropna())
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    
    # Scatter Plot - Likes vs Impressions
    st.subheader("📊 Relationship Between Likes and Impressions")
    fig = px.scatter(data, x="Impressions", y="Likes", size="Likes", trendline="ols")
    st.plotly_chart(fig)
    
    # Correlation Analysis
    st.subheader("📌 Correlation with Impressions")
    numeric_data = data.select_dtypes(include=['number'])
    correlation = numeric_data.corr()
    st.write(correlation["Impressions"].sort_values(ascending=False))
    
    # Conversion Rate
    st.subheader("📌 Instagram Conversion Rate")
    conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
    st.metric("Conversion Rate", f"{conversion_rate:.2f}%")
