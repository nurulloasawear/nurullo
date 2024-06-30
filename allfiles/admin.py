import pandas as pd
import matplotlib.pyplot as plt

# Loyihaning asosiy bosqichlari
tasks = [
    'Talablarni Yig\'ish va Kelishish',
    'Texnik Spetsifikatsiya va Yetkazib Beruvchi Tanlash',
    'Tizimni O\'rnatish va Integratsiya',
    'Foydalanuvchilarni O\'qitish va Tizimni Ishga Tushirish'
]

# Bosqichlar uchun vaqt jadvali
start_dates = [
    '2024-07-01',
    '2024-08-01',
    '2024-09-01',
    '2024-11-01'
]

end_dates = [
    '2024-07-31',
    '2024-08-31',
    '2024-10-31',
    '2024-12-31'
]

# DataFrame yaratish
df = pd.DataFrame({
    'Task': tasks,
    'Start': pd.to_datetime(start_dates),
    'End': pd.to_datetime(end_dates)
})

# Gantt chart yaratish
plt.figure(figsize=(10, 6))
plt.barh(df['Task'], (df['End'] - df['Start']).dt.days, left=df['Start'])
plt.xlabel('Vaqt')
plt.ylabel('Vazifalar')
plt.title('LMS Joriy Etish Loyihasi - Gantt Chart')
plt.grid(axis='x')

# Loyihaning har bir bosqichi uchun vaqt jadvali
for idx, row in df.iterrows():
    plt.text(row['Start'], idx, row['Start'].strftime('%Y-%m-%d'), va='center', ha='right')
    plt.text(row['End'], idx, row['End'].strftime('%Y-%m-%d'), va='center', ha='left')

plt.tight_layout()
plt.show()
