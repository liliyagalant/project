# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
a = input("введите номер месяца: ")
if a=="1":
    print(f" в Январе 31 день ")
if a=="2":
    print(f" в Феврале 28 дней ")
if a=="3":
    print(f" в Марте 31 день ")
if a=="4":
    print(f" в Апреле 30 дней ")
if a=="5":
    print(f" в Мае 31 день ")
if a=="6":
    print(f" в Июне 30 дней ")
if a=="7":
    print(f" в Июле 31 день ")
if a=="8":
    print(f" в Августе 31 дней ")
if a=="9":
    print(f" в Сентябре 30 день ")
if a=="10":
    print(f" в Октябре 31 дней ")
if a=="11":
    print(f" в Ноябре 30 дней ")
if a=="12":
    print(f" в Декабре 31 день ")
elif int(a)>12 or int(a)<1:
    print ("введите корректную дату!")