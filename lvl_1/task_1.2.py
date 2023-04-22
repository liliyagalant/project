# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random

random_songs = random.sample(my_favorite_songs, 3)

total_duration = sum(song[1] for song in random_songs)

print(f"Три песни звучат {total_duration:.2f} минут")


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
random_songs = random.sample(list(my_favorite_songs_dict.keys()), 3)

# Calculate the total duration of the selected songs
total_duration = sum(my_favorite_songs_dict[song] for song in random_songs)

# Print the result in the desired format
print(f"Три песни звучат {total_duration:.2f} минут")
# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
print(f"{random_songs[0]}, {random_songs[1]} и {random_songs[2]}")

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

from datetime import datetime, timedelta


random_songs = random.sample(list(my_favorite_songs_dict.keys()), 3)


total_duration_minutes = sum(my_favorite_songs_dict[song] for song in random_songs)


total_duration_timedelta = timedelta(minutes=total_duration_minutes)


base_datetime = datetime(1900, 1, 1)


total_duration_datetime = base_datetime + total_duration_timedelta


total_duration_string = total_duration_datetime.strftime('%H:%M:%S')


print(f"Три песни звучат {total_duration_string}")

