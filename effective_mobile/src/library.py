# Импортируем модули
# json - для работы с данными в формате json
# uuid - для генерации уникальных идентификаторов
# pathlib - для поиска пути к файлу относительно корневой директории

import json
import uuid
from pathlib import Path

class Library:
    """
    Класс для управления книгами в библиотеке.

    Attributes:
        id (str): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Текущий статус книги (по умолчанию "в наличии").
    """
    
    # Указываем путь к файлу с данными
    BOOKS_FILE = Path(__file__).resolve().parents[1] / 'data' / 'book.json'

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализация книги.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
            status (str, optional): Текущий статус книги (по умолчанию "в наличии").
        """
        # Генерация уникального идентификатора
        self.id = str(uuid.uuid4())

        # Назначение атрибутов
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    @staticmethod
    def __load_books():
        """
        Чтение данных из файла библиотеки.

        Returns:
            list: Список словарей, где каждый словарь содержит данные о книге.
        """
        try:
            # Открытие файла в режиме чтения с кодировкой utf-8
            with open(Library.BOOKS_FILE, "r", encoding="utf-8") as file:
                # Чтение данных из файла и возврат списка словарей
                return json.load(file)
        except FileNotFoundError:
            # Возврат пустого списка, если файл не найден
            return []
        except json.JSONDecodeError:
            # Вывод сообщения об ошибке и возврат пустого списка, если данные не могут быть декодированы
            print("Ошибка чтения файла данных.")
            return []

    @staticmethod
    def __save_books(books):
        """
        Запись данных в файл библиотеки.

        Args:
            books (list): Список словарей, где каждый словарь содержит данные о книге.
        """
        try:
            # Открытие файла в режиме записи с кодировкой utf-8
            with open(Library.BOOKS_FILE, "w", encoding="utf-8") as file:
                # Запись данных в файл
                json.dump(books, file, ensure_ascii=False, indent=4)
        except Exception as e:
            # Вывод сообщения об ошибке
            print(f"Ошибка записи в файл данных: {e}")

    @staticmethod
    def add_book(title: str, author: str, year: int):
        """
        Добавление книги в библиотеку.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.

        Returns:
            None
        """
        try:
            # Чтение данных из файла библиотеки
            books = Library.__load_books()

            # Создание нового объекта класса Library и конвертация его атрибутов в словарь
            new_book = Library(title, author, year).__dict__

            # Добавление нового объекта в список библиотеки
            books.append(new_book)

            # Запись изменений в файл библиотеки
            Library.__save_books(books)

            # Вывод сообщения об успешном добавлении книги
            print(f"Книга '{title}' добавлена с ID {new_book['id']}")

        except Exception as e:
            # Вывод сообщения об ошибке
            print(f"Ошибка при добавлении книги: {e}")

    @staticmethod
    def delete_book(book_id: str):
        """
        Удаление книги из библиотеки по ее ID.

        Args:
            book_id (str): Идентификатор книги для удаления.

        Returns:
            None
        """
        try:
            # Чтение данных из файла библиотеки
            books = Library.__load_books()

            # Проверка наличия книги с указанным ID
            book_exists = any(book['id'] == book_id for book in books)

            # Если книги не найдена, выводим сообщение и возвращаемся
            if not book_exists:
                print(f"Книга с ID {book_id} не найдена.")
                return

            # Удаление книги из списка библиотеки
            books = [book for book in books if book['id'] != book_id]

            # Запись изменений в файл библиотеки
            Library.__save_books(books)

            # Вывод сообщения об успешном удалении книги
            print(f"Книга с ID {book_id} удалена.")
        except Exception as e:
            # Вывод сообщения об ошибке
            print(f"Ошибка при удалении книги: {e}")

    @staticmethod
    def find_books_by_title(title: str) -> list:
        """
        Поиск книги по ее названию.

        Args:
            title (str): Название книги.

        Returns:
            list: Список книг, соответствующих запросу.
        """
        # загрузка данных из файла библиотеки
        books = Library.__load_books()

        # поиск книги по ее названию без учета регистра
        result = [book for book in books if title.lower() in book['title'].lower()]
        
        if len(result) == 0:
            print(f"Книга с названием {title} не найдена.")
            
        return result

    @staticmethod
    def find_books_by_author(author: str) -> list:
        """
        Поиск книги по автору.

        Args:
            author (str): Имя автора книги.

        Returns:
            list: Список книг, написанных автором.
        """
        # загрузка данных из файла библиотеки
        books = Library.__load_books()

        # поиск книги по автору без учета регистра
        result = [book for book in books if author.lower() in book['author'].lower()]
        
        if len(result) == 0:
            print(f"Книга с автором {author} не найдена.")
            
        return result

    @staticmethod
    def find_books_by_year(year: int) -> list:
        """
        Поиск книги по году издания.

        Args:
            year (int): Год издания книги.

        Returns:
            list: Список книг, соответствующих запросу.
        """
        # загрузка данных из файла библиотеки
        books = Library.__load_books()

        # поиск книги по году издания
        result =  [book for book in books if book['year'] == year]
        
        if len(result) == 0:
            print(f"Книга с годом издания {year} не найдена.")
            
        return result
    
    @staticmethod
    def display_books():
        """
        Вывод информации о всех книгах из списка.

        Выводит информацию о каждой книге в следующем формате:
        ID: <id книги>, Название: <название книги>, Автор: <автор книги>, Год издания: <год издания>, Статус: <статус книги>
        """
        books = Library.__load_books()  # загрузка данных из файла библиотеки

        for book in books:  # перебираем каждую книгу в списке
            print(
                f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
                f"Год издания: {book['year']}, Статус: {book['status']}"
            )  # выводим информацию о книге

    @staticmethod
    def update_book_status(book_id: str, status: str):
        """
        Обновление статуса книги по ее ID.

        Args:
            book_id (str): Идентификатор книги для обновления статуса.
            status (str): Новый статус книги.

        Returns:
            None
        """
        try:
            # Загрузка данных из файла библиотеки
            books = Library.__load_books()

            # Перебор книг в списке, поиск книги с указанным ID
            book_found = False
            for book in books:
                if book['id'] == book_id:
                    # Обновление статуса книги и вывод сообщения об обновлении
                    book['status'] = status
                    print(f"Статус книги с ID {book_id} обновлен на '{status}'")
                    book_found = True
                    break

            # Если книги не найдена, вывод сообщения об этом
            if not book_found:
                print(f"Книга с ID {book_id} не найдена.")

            # Сохранение изменений в файл библиотеки
            Library.__save_books(books)

        except Exception as e:
            # Вывод сообщения об ошибке
            print(f"Ошибка при обновлении статуса книги: {e}")
