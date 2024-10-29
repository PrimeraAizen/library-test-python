import json


books = []


class Book:
    title = ""
    author = ""
    year = 0
    status = ""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def __dict__(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


def save():
    res = {}
    for index, value in enumerate(books):
        res[index] = value
    with open("books.json", 'w') as f:
        json.dump(res, f)


def get_books():
    try:
        with open("books.json", "r") as f:
            try:
                res = json.load(f)
            except json.JSONDecodeError:
                return []
        return list(res.values())
    except FileNotFoundError:
        open("books.json", "x")
        return []


def search_title(text: str) -> list:
    return [book for book in books if text in book['title']]


def search_author(text: str) -> list:
    return [book for book in books if text in book['author']]


def search_year(year: int) -> list:
    return [book for book in books if book['year'] == year]


def search(option: int, text: str):
    if option == 1:
        return search_title(text)
    if option == 2:
        return search_author(text)
    if option == 3:
        return search_year(int(text))


def delete(id: int):
    for index, book in enumerate(books):
        if index == id - 1:
            books.pop(index)
            save()
            return "Deleted"
    return "Not found"


def update_status(id: int, status: str):
    for index, book in enumerate(books):
        if index == id:
            book['status'] = status
            save()
            return True
    return False


def menu():
    print("Меню:")
    print("1. Показать все книги")
    print("2. Добавить книгу")
    print("3. Найти книгу")
    print("4. Удалить книгу")
    print("5. Обновить статус книги")
    print("6. Выйти")
    try:
        return int(input("Выберите опцию: "))
    except ValueError:
        print("Неверная опция")
        return 0


if __name__ == '__main__':
    books = get_books()
    while True:
        option = menu()
        match option:
            case 1:
                for index, book in enumerate(books):
                    print(f"{index+1}. {book['title']}, {book['author']}, {book['year']}, {book['status']}")
            case 2:
                print("0. Выход")
                in_str = input("Введите название книги, автора и год через запятую: ")
                if in_str == "0":
                    continue
                try:
                    title, author, year = in_str.split(",")
                    books.append(Book(title, author, int(year)).__dict__())
                    save()
                    print("Книга добавлена")
                except ValueError:
                    print("Неверный формат")
                    continue
            case 3:
                print("0. Выход")
                in_str = input("Введите опцию поиска (1 - название, 2 - автор, 3 - год) и текст через запятую: ")
                if in_str == "0":
                    continue
                try:
                    option, text = in_str.split(",")
                    print(search(int(option), text))
                except ValueError:
                    print("Неверный формат")
                    continue
            case 4:
                print("0. Выход")
                id = int(input("Введите id книги: "))
                if id == 0:
                    continue
                print(delete(id))
            case 5:
                print("0. Выход")
                id = int(input("Введите id книги: "))
                if id == 0:
                    continue
                status = input("Введите статус книги: ")
                print(update_status(id, status))
            case 6:
                break
            case _:
                print("Неверная опция")
                continue



print("blablablablalbalbal")
