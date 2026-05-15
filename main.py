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


def add_book():
    books = load_books()

    author = input("Автор: ")
    title = input("Название: ")

    rating = int(input("Оценка: "))
    date = input("Дата: ")

    book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    }

    books.append(book)

    save_books(books)

    print("Книга добавлена")


def main():
    while True:
        print("\n1. Добавить книгу")
        print("6. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            add_book()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()