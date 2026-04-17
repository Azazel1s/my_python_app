try:
    number = int(input("Введіть ціле число: "))
    if number % 2 == 0:
        print(f"Число {number} — парне.")
    else:
        print(f"Число {number} — непарне.")
except ValueError:
    print("Помилка: введіть ціле число!")