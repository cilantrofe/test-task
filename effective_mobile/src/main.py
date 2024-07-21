# Импортируем модули 
# для добавления, удаления, поиска книг, а также для изменения статуса книги.

from library import Library

def main():
    """
    Главный цикл программы.
    """
    while True:
        try:
            # Вывод меню
            print("\nСистема управления библиотекой")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Искать книгу")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выход")

            # Чтение выбора пользователя
            choice = input("Выберите действие: ")

            if choice == '1':
                # Добавление книги
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                Library.add_book(title, author, year)
            elif choice == '2':
                # Удаление книги
                book_id = input("Введите ID книги для удаления: ")
                Library.delete_book(book_id)
            elif choice == '3':
                # Поиск книги
                print("1. Искать по названию")
                print("2. Искать по автору")
                print("3. Искать по году")
                search_choice = input("Выберите действие: ")
                if search_choice == '1':
                    title = input("Введите название книги: ")
                    results = Library.find_books_by_title(title)
                elif search_choice == '2':
                    author = input("Введите автора книги: ")
                    results = Library.find_books_by_author(author)
                elif search_choice == '3':
                    year = int(input("Введите год издания книги: "))
                    results = Library.find_books_by_year(year)
                else:
                    print("Некорректный выбор")
                    continue

                # Вывод результатов поиска
                for book in results:
                    print(f"ID: {book['id']}, Название: {book['title']}, "
                          f"Автор: {book['author']}, Год издания: "
                          f"{book['year']}, Статус: {book['status']}")
            elif choice == '4':
                # Отображение всех книг
                Library.display_books()
            elif choice == '5':
                # Изменение статуса книги
                book_id = input("Введите ID книги: ")
                status = input("Введите новый статус (в наличии/выдана): ")
                Library.update_book_status(book_id, status)
            elif choice == '6':
                # Выход из программы
                break
            else:
                print("Некорректный выбор. Пожалуйста, попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
