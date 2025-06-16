import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Administrator/Desktop/playlist/matplotlip/project/netflix_titles.csv.zip")

df = df[df['type'] == 'Movie']
df['duration'] = df['duration'].str.replace('min', "").astype(float)
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

def duration_bucket(d):
    if d < 60:
        return 'Short'
    elif d <= 120:
        return 'Medium'
    else:
        return 'Long'

df["duration_category"] = df['duration'].apply(duration_bucket)

year_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 5))
plt.title('Number of Movie Released Per Year')
plt.xlabel('Year')
plt.ylabel("Count")
plt.grid(True)
plt.show()


df['genre_primary'] = df['listed_in'].str.split(',').str[0]

genre_count = df['genre_primary'].value_counts().head(10)

plt.figure(figsize=(10,6))
genre_count.plot(kind='barh', color='skyblue')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Movies')
plt.show()


from collections import Counter

cast = df['cast'].dropna()

all_actors = []
for entry in cast:
    all_actors.extend(entry.split(', '))

actor_count = Counter(all_actors).most_common(10)
actors, counts = zip(*actor_count)
plt.figure(figsize=(10,6))
plt.barh(actors[::-1], counts[::-1], color = 'salmon')
plt.title('Top 10 Most Featured Actors')
plt.xlabel('Number of Movies')
plt.show()

plt.figure(figsize=(6, 6))
df['duration_category'].value_counts().plot.pie(autopct = '%1.1f%%', startangle=140)
plt.title('Movie Duration Categories')
plt.ylabel("")
plt.show()