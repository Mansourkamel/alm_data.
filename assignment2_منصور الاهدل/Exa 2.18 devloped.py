import requests
import pandas as pd
import time
import random
from datetime import datetime, timedelta


api_key = "YOUR_API_KEY"  
cities = ["Sanaa", "London", "Tokyo", "New York", "Cairo", "Paris", "Moscow", "Toronto", "Istanbul", "Sydney"]
weather_records = []

for day_offset in range(10):
    current_time = datetime.now() + timedelta(days=day_offset)
    for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            record = {
                "City": city,
                "Datetime": current_time.strftime('%Y-%m-%d %H:%M:%S'),
                "Temp_Min": data["main"]["temp_min"],
                "Temp_Max": data["main"]["temp_max"],
                "Weather": data["weather"][0]["description"]
            }
            weather_records.append(record)
        else:
            print(f"فشل جلب البيانات من: {city}")
        time.sleep(1) 

df = pd.DataFrame(weather_records)


df.dropna(inplace=True)

df.drop_duplicates(inplace=True)


df['Datetime'] = pd.to_datetime(df['Datetime'])


print("وصف موجز للبيانات:")
print(df.describe())


print("\nعدد القراءات لكل مدينة:")
print(df['City'].value_counts())


print("\nمتوسط الحرارة لكل مدينة:")
print(df.groupby('City')[['Temp_Min', 'Temp_Max']].mean())


df.reset_index(drop=True, inplace=True)


print("\nعدد القيم الفريدة:")
print(df.nunique())


df.to_csv("weather_data.csv", index=False)

print("\n تم الانتهاء من جمع وتنظيف وتصدير البيانات بنجاح.")
