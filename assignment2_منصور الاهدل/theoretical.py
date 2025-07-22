import pandas as pd
import numpy as np

# =================== 1. قراءة البيانات ===================
df = pd.read_csv('bank_loans_data.csv')

print(" تم قراءة البيانات.")
print(f"عدد السجلات قبل التنظيف: {len(df)}")

# =================== 2. تنظيف البيانات ===================
# تحويل العمر إلى رقم
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# معالجة القيم الناقصة
df.fillna({
    'salary': df['salary'].median(),
    'loan_amount': df['loan_amount'].median(),
    'gender': 'Unknown',
    'job_title': 'Unknown',
    'contract_type': 'Unknown',
    'repayment_status': 'Unknown'
}, inplace=True)

# إزالة التكرارات
df.drop_duplicates(subset=['client_id'], keep='first', inplace=True)

# معالجة القيم الشاذة
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['salary'] < (Q1 - 1.5 * IQR)) | (df['salary'] > (Q3 + 1.5 * IQR)))]

print(" 2. تم تنظيف البيانات.")
print(f"عدد السجلات بعد التنظيف: {len(df)}")

# =================== 3. تصنيف الفئات العمرية ===================
bins = [20, 29, 39, 49, 59, 70]
labels = ['20-29', '30-39', '40-49', '50-59', '60-70']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

print(" 3. تم إضافة الفئة العمرية.")

# =================== 4. تحليل أولي ===================
# عدد العملاء حسب نوع التعاقد
contract_counts = df['contract_type'].value_counts()
print("\n عدد العملاء حسب نوع التعاقد:")
print(contract_counts)

# متوسط القرض لكل فئة عمرية
avg_loan_by_age = df.groupby('age_group')['loan_amount'].mean()
print("\n متوسط مبلغ القرض حسب الفئة العمرية:")
print(avg_loan_by_age)

# نسبة التخلف عن السداد حسب المدينة
default_by_city = df.groupby('city')['repayment_status'].apply(lambda x: ((x == 'Default') | (x == 'Late')).mean() * 100)
print("\نسبة التخلف عن السداد حسب المدينة (%):")
print(default_by_city)

# =================== 5. حفظ البيانات المعالجة ===================
df.to_csv('cleaned_bank_loans_data.csv', index=False)
print("\n 5. تم حفظ البيانات المعالجة في ملف: cleaned_bank_loans_data.csv")