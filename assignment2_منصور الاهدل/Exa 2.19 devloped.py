import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


news_sources = {
    "BBC Arabic": "https://www.bbc.com/arabic",
    "Al Jazeera Arabic": "https://www.aljazeera.net/news",
    "CNN English": "https://edition.cnn.com/world",
    "Reuters English": "https://www.reuters.com/news/archive/worldNews"
}

news_data = []


for name, url in news_sources.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    if "bbc" in url:
        titles = soup.find_all('h3')
    elif "aljazeera" in url:
        titles = soup.find_all('h1') + soup.find_all('h2')
    elif "cnn" in url:
        titles = soup.find_all('span', class_='container__headline-text')
    elif "reuters" in url:
        titles = soup.find_all('h3', class_='story-title') or soup.find_all('h3')

    
    for t in titles[:10]: 
        text = t.get_text(strip=True)
        if len(text) > 10:
            news_data.append({
                "Source": name,
                "Title": text,
                "Datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })


df = pd.DataFrame(news_data)
df.to_csv("news_data.csv", index=False)
print("تم حفظ العناوين في news_data.csv")

# قراءة الملف
df = pd.read_csv("news_data.csv")


print("عدد الصفوف:", df.shape[0])
print("عدد الأعمدة:", df.shape[1])
print(df.head())

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print("\nعدد العناوين حسب كل مصدر:")
print(df['Source'].value_counts())

print("\nالوصف الإحصائي:")
print(df.describe(include='all'))


df['Length'] = df['Title'].apply(len)  
df['Language'] = df['Title'].apply(lambda t: 'Arabic' if any('\u0600' <= c <= '\u06FF' for c in t) else 'English')

print("\nعدد العناوين حسب اللغة:")
print(df['Language'].value_counts())

longest_title = df.loc[df['Length'].idxmax()]
print("\n أطول عنوان:")
print(longest_title)


sorted_df = df.sort_values(by='Length', ascending=False)

print("\nعدد العناوين الفريدة:", df['Title'].nunique())


df.to_csv("cleaned_news_data.csv", index=False)
