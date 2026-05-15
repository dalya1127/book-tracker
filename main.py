import json

FILE_NAME = "books.json"


def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def main():
    while True:
        print("\nТрекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт: ")

        if choice == "6":
            print("Выход")
            break


if __name__ == "__main__":
    main()