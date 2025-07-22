print('-----------------Ex:2.1------------------------')
import pandas as pd

d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3':
[7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print(df)
print('-----------------Ex:2.2------------------------')
count_column = df.shape[1]
print("Number of columns:")
print(count_column)
count_row = df.shape[0]
print("Number of rows:")
print(count_row)
print('-----------------Ex:2.3------------------------')
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data)
print('-------------------Ex:2.4----------------------')
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data.head())
print('------------------Ex:2.5-----------------------')
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True)
print(health_data)
print('-----------------Ex:2.6------------------------')
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True)
df.fillna(df.mean(),inplace=True)
print('------------------Ex:2.7-----------------------')
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True)
df.fillna(df.mean(),inplace=True)
df.drop_duplicates(inplace=True)
print('-------------------Ex:2.8----------------------')
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data.info)
print('--------------------Ex:2.9---------------------')
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.dropna(axis=0, inplace=True)

health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print(health_data.info())
print('-------------------Ex:2.10----------------------')
import pandas as pd

health_data = pd.read_csv("data.csv", header=0, sep=",")
pd.set_option('display.max_columns', None)
print(health_data.describe())
print('------------------Ex:2.11-----------------------')
import pandas as pd
data={
    'Name':['Ali','Fatima','Omar'],
    'Age':[25,22,30],
    'City':['Sanna','Aden','Taiz']
}
df=pd.DataFrame(data)
print(df)
print('---------------------Ex:2.12--------------------')
import pandas as pd
health_data = pd.read_csv("data.csv", header=0, sep=",")
health_data.dropna(axis=0,inplace=True)
df.fillna(df.mean(),inplace=True)
df.drop_duplicates(inplace=True)
filtered_df =df[df['Age']> 25]
print( filtered_df)
print('-----------------Ex:2.13------------------------')
grouped=df.groupby( 'City' ) ['Age']. mean()
print(grouped)
print('-----------------Ex:2.14------------------------')
print(df.describe())
print('Mean age:',df['Age'].mean())
print("Deviation Standard:",df['Age'].std())
print('-----------------Ex:2.15------------------------')

data2={
    'City':['Sanaa','Aden','Taiz'],
    'Population':[2_500_000,800_000,600_000]
}
df2=pd.DataFrame(data2)
merged_df=pd.merge(df,df2 ,on='City')
print(merged_df)
print('-----------------Ex:2.16------------------------')
df.to_csv('output.cv',index=False)
df.to_excel('output.xlsx',sheet_name='pepole')
print('-----------------Ex:2.17------------------------')
sales=pd.read_csv('sales_data.csv' )
print (sales. head (3))
high_sales= sales[sales['Revenue']>100]
product_sales =sales.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
product-sales.to_excel('product_report.xlsx')

print('-----------------Ex:2.18------------------------')
import requests
api_key = ""
city = "Sana'a"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json() 

print(data['main']['temp']) 
print('-----------------Ex:2.19------------------------')
from bs4 import BeautifulSoup
import requests


url = "https://www.bbc.com/arabic"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_titles = soup.find_all('h3')  
for title in news_titles[:5]:  
    print(title.get_text())
