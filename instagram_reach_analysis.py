
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor

"""# Read Data"""

data = pd.read_csv("Instagram data.csv", encoding = 'latin1')

print(data.head())

"""# Whether the dataset contains null values or not"""

data.isnull().sum()

data = data.dropna()

"""# Look at the insights of the columns to understand the data type of all the columns:"""

data.info()

"""# Analyzing Instagram Reach

- Let’s start with analyzing the reach of my Instagram posts.
- I will first have a look at the distribution of impressions I have received from home.
"""

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
#sns.distplot(data['From Home'])
sns.histplot(data['From Home'])
plt.show()

"""# Impression

- The impressions I get from the home section on Instagram shows how much my posts reach my followers.

- Looking at the impressions from home, I can say it’s hard to reach all my followers daily.

- Now let’s have a look at the distribution of the impressions I received from hashtags:
"""

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
#sns.distplot(data['From Hashtags'])
sns.histplot(data['From Hashtags'])
plt.show()

"""# Hashtag

- Hashtags are tools we use to categorize our posts on Instagram so that we can reach more people based on the kind of content we are creating.

- Looking at hashtag impressions shows that not all posts can be reached using hashtags, but many new users can be reached from hashtags.

- Now let’s have a look at the distribution of impressions I have received from the explore section of Instagram:
"""

plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Explore")
#sns.distplot(data['From Explore'])
sns.histplot(data['From Explore'])
plt.show()

"""- The explore section of Instagram is the recommendation system of Instagram. It recommends posts to users based on their preferences and interests.

- By looking at the impressions I have received from the explore section, I can say that Instagram does not recommend our posts much to the users. Some posts have received a good reach from the explore section, but it’s still very low compared to the reach I receive from hashtags.

- Let’s have a look at the percentage of impressions I get from various sources on Instagram:
"""

home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home','From Hashtags','From Explore','Other']
values = [home, hashtags, explore, other]

fig = px.pie(data, values=values, names=labels,
             title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()

"""#### So the above donut plot shows that almost 45 percent of the reach is from my followers, 33.6 percent is from hashtags, 19.2 percent is from the explore section, and 3.05 percent is from other sources.

# Analyzing Content

- Let’s analyze the content of my Instagram posts. The dataset has two columns, namely caption, and hashtags, which will help us understand the kind of content I post on Instagram.

- Let’s create a wordcloud of the caption column to look at the most used words in the caption of my Instagram posts:
"""

text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.style.use('classic')
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

"""- Let’s create a wordcloud of the hashtags column to look at the most used hashtags in my Instagram posts:"""

text = " ".join(i for i in data.Hashtags)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
plt.figure( figsize=(12,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

"""# Analyzing Relationships

- Let’s analyze relationships to find the most important factors of our Instagram reach. It will also help us in understanding how the Instagram algorithm works.

- Let’s have a look at the relationship between the number of likes and the number of impressions on my Instagram posts:
"""

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Likes", size="Likes", trendline="ols",
                    title = "Relationship Between Likes and Impressions")
figure.show()

"""- There is a linear relationship between the number of likes and the reach I got on Instagram.

- Let’s see the relationship between the number of comments and the number of impressions on my Instagram posts:
"""

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Comments", size="Comments", trendline="ols",
                    title = "Relationship Between Comments and Total Impressions")
figure.show()

"""- It looks like the number of comments we get on a post doesn’t affect its reach.

- Lets have a look at the relationship between the number of shares and the number of impressions:
"""

figure = px.scatter(data_frame = data, x="Impressions",
                    y="Shares", size="Shares", trendline="ols",
                    title = "Relationship Between Shares and Total Impressions")
figure.show()

"""- There is a linear relationship between the number of times my post is saved and the reach of my Instagram post.

- Let’s have a look at the correlation of all the columns with the Impressions column:
"""
numeric_data = data.select_dtypes(include=['number']) 
correlation = numeric_data.corr()
print(correlation["Impressions"].sort_values(ascending=False))

"""- So we can say that more likes and saves will help you get more reach on Instagram.

- The higher number of shares will also help you get more reach, but a low number of shares will not affect your reach either.

# Analyzing Conversion Rate

- In Instagram, conversation rate means how many followers you are getting from the number of profile visits from a post.

- The formula that you can use to calculate conversion rate is (Follows/Profile Visits) * 100. Now let’s have a look at the conversation rate of my Instagram account:
"""

conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(conversion_rate)

"""- So the conversation rate of my Instagram account is 31% which sounds like a very good conversation rate.

- Let’s have a look at the relationship between the total profile visits and the number of followers gained from all profile visits:
"""

figure = px.scatter(data_frame = data, x="Profile Visits",
                    y="Follows", size="Follows", trendline="ols",
                    title = "Relationship Between Profile Visits and Followers Gained")
figure.show()

"""#### The relationship between profile visits and followers gained is also linear."""