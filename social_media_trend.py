import pandas as pd
df = pd.read_csv('E:\excel\sentimentdataset.csv')
# print(df)


df['Sentiment_Clean'] = df['Sentiment'].str.strip()
df['Country_Clean'] = df['Country'].str.strip()
df['Platform_Clean'] = df['Platform'].str.strip()
df.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Year', 'Month', 'Day', 'Hour'], axis=1, inplace= True)
df['Retweets'] = df['Retweets'].astype(int)
df['Likes'] = df['Likes'].astype(int)
df.info()
df.to_csv('social_media_trend.csv', index=False)

# print(ch)
