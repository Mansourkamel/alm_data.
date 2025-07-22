import pandas as pd
data={
    'Name':['Ali','Fatima','Omar'],
    'Age':[25,22,30],
    'City':['Sanna','Aden','Taiz']
}
df=pd.DataFrame(data)
print('-----------1----------------')
print(df['Age'].apply(lambda x: x + 1))
print('-----------2----------------')
print(df.query('Age > 25 and City == "Taiz"'))
print('-----------3----------------')
print(df[df['City'].isin(['Sanaa', 'Aden'])])
print('-----------4----------------')
print(df.sort_values(by='Age', ascending=False))
print('-----------5----------------')
print(df['City'].value_counts())
print('-----------6----------------')
print(df['City'].map({'Sanaa': 'صنعاء', 'Aden': 'عدن'}))
print('-----------7----------------')
print(df.reset_index(drop=True))
print('-----------8----------------')
print(df.set_index('Name'))
print('-----------9----------------')
print(df.duplicated())
print('-----------10----------------')
print(df.nunique())
