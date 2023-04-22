# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# первый трек
first_song = my_favorite_songs[:my_favorite_songs.index(',')]
print(first_song)

# последний трек
last_song = my_favorite_songs[my_favorite_songs.rindex(',')+2:]
print(last_song)

# второй трек
second_song = my_favorite_songs[my_favorite_songs.index(',')+2:my_favorite_songs.index(',', my_favorite_songs.index(',')+1)]
print(second_song)

# второй с конца трек
second_to_last_song = my_favorite_songs[my_favorite_songs.rindex(',', 0, my_favorite_songs.rindex(','))-1:my_favorite_songs.rindex(',')]
print(second_to_last_song)
