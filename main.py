import pandas as pd
import random

# Генерируем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем список уникальных значений в столбце
unique_values = data['whoAmI'].unique()


# Функция для преобразования строк в one-hot кодировку
def one_hot_encode(value):
    encoded = [0] * len(unique_values)
    encoded[list(unique_values).index(value)] = 1
    return encoded


# Применяем one-hot кодировку к столбцу
one_hot_encoded = data['whoAmI'].apply(one_hot_encode)

# Создаем новый DataFrame с one hot закодированными столбцами
one_hot_data = pd.DataFrame(one_hot_encoded.tolist(), columns=unique_values, index=data.index)

# Объединяем исходный DataFrame и one-hot закодированный DataFrame
final_data = pd.concat([data, one_hot_data], axis=1)

print(final_data.head())
