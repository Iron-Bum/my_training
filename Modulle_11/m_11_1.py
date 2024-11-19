import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Name': ['Сергей', 'Инна', 'Мила'],
    'Приход': [1400, 990, 730],
    'Уход': [780, 200, 490]
}

# Создаю условную таблицу
df = pd.DataFrame(data)
print(df)

# Переименовываю столбец
df = df.rename(columns={'Name': 'Имя'})

# Изменяю значение ячейки
df.at[0, 'Приход'] = 1700

# Сохраняю результат в файл
df.to_csv('M_11.csv', index=False)


# Печать DataFrame
print("DataFrame:")
print(df)

# Визуализация данных
plt.figure(figsize=(10, 6))

# Установка позиций для столбцов
bar_width = 0.35
index = range(len(df))

# Столбцы для Прихода и Ухода
plt.bar(index, df['Приход'], bar_width, label='Приход', color='green')
plt.bar([i + bar_width for i in index], df['Уход'], bar_width, label='Уход', color='red')

# Настройка графика
plt.xlabel('Имя')
plt.ylabel('Сумма')
plt.title('Приходы и Уходы')
plt.xticks([i + bar_width / 2 for i in index], df['Имя'])  # Изменение меток по оси X
plt.legend()

# Показать график
plt.tight_layout()
plt.show()

