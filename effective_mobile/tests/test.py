# Импортируем модули
# unittest - для тестирования
# os - для работы с файлами
# json - для работы с данными в формате json
# pathlib - для поиска пути к файлу относительно корневой директории

import unittest
import os
import json
from pathlib import Path

# Импортируем модуль библиотеки
from src.library import Library

class TestLibrary(unittest.TestCase):
    """
    Класс для тестирования библиотеки
    """
    def setUp(self):
        """
        Установка данных для тестирования
        """
        # Устанавливаем файл с данными
        self.test_file = Library.BOOKS_FILE

        # Устанавливаем данные для тестирования
        self.books_data = [
            {
                "id": "f53ad9f0-e403-4a13-b72a-09f5fa72e51e",
                "title": "Цитадель",
                "author": "Арчибальд Кронин",
                "year": 2022,
                "status": "в наличии"
            },
            {
                "id": "22fc941a-866d-48a3-8078-57079f6b5b85",
                "title": "Крутой маршрут",
                "author": "Евгения Гинзбург",
                "year": 2022,
                "status": "в наличии"
            },
            {
                "id": "3bbacdbb-de68-4550-9592-c232874bc6d6",
                "title": "На краю света",
                "author": "Сергей Безбородов",
                "year": 2019,
                "status": "в наличии"
            },
            {
                "id": "9e7f6731-b1f1-4651-b438-3956c117ef1b",
                "title": "Пикник на обочине",
                "author": "Аркадий и Борис Стругацкие",
                "year": 2023,
                "status": "в наличии"
            }
        ]

        # Запись данных в файл
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(self.books_data, f, ensure_ascii=False, indent=4)

    def tearDown(self):
        """
        Удаляет файл с данными после завершения тестов.
        """
        # Проверяем существование файла
        if os.path.exists(self.test_file):
            # Удаляем файл
            os.remove(self.test_file)

    def test_add_book(self):
        """
        Тестирование функции add_book.
        """
        # Добавление книги
        Library.add_book('Педагогическая поэма', 'Антон Макаренко', 2020)

        # Чтение данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Проверка количества книг
        self.assertEqual(len(books), 5)

        # Проверка атрибутов последней книги
        last_book = books[-1]
        self.assertEqual(last_book['title'], 'Педагогическая поэма')
        self.assertEqual(last_book['author'], 'Антон Макаренко')
        self.assertEqual(last_book['year'], 2020)
        self.assertEqual(last_book['status'], 'в наличии')

    def test_find_books_by_title(self):
        """
        Тестирование функции find_books_by_title.
        Проверяет, что функция возвращает корректный список книг
        по заданному названию.
        """
        # Искать книгу по названию
        results = Library.find_books_by_title('Цитадель')

        # Проверяем количество найденных книг
        self.assertEqual(len(results), 1)

        # Проверяем название найденной книги
        self.assertEqual(results[0]['title'], 'Цитадель')
        
    def test_find_books_by_nonexistent_title(self):
        """
        Тестирование функции find_books_by_title.
        Проверяет, что функция возвращает пустый список книг
        по названию, которого не существует.
        """
        # Искать книгу по названию
        results = Library.find_books_by_title('nonexistent_title')

        # Проверяем количество найденных книг
        self.assertEqual(len(results), 0)
        
        self.assertTrue("Книга с названием nonexistent_title не найдена.")

    def test_find_books_by_author(self):
        """
        Тестирование функции find_books_by_author.
        Проверяет, что функция возвращает корректный список книг
        по заданному автору.
        """
        # Искать книги по автору
        results = Library.find_books_by_author('Евгения Гинзбург')

        # Проверяем количество найденных книг
        self.assertEqual(len(results), 1)

        # Проверяем автора найденной книги
        self.assertEqual(results[0]['author'], 'Евгения Гинзбург')

    def test_find_books_by_year(self):
        """
        Тестирование функции find_books_by_year.
        Проверяет, что функция возвращает корректный список книг
        по заданному году издания.
        """
        # Искать книги по году издания
        results = Library.find_books_by_year(2022)

        # Проверяем количество найденных книг
        self.assertEqual(len(results), 2)

        # Проверяем год издания первой и второй найденной книги
        self.assertEqual(results[0]['year'], 2022)
        self.assertEqual(results[1]['year'], 2022)

    def test_display_books(self):
        """
        Тестирование функции display_books.
        Проверяет, что функция отображает корректный список книг.
        """
        # Отображение списка книг
        Library.display_books()

        # Чтение данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Проверка количества книг
        self.assertEqual(len(books), 4)

    def test_update_book_status(self):
        """
        Тестирование функции update_book_status.

        Проверяет, что функция обновляет статус книги по её ID.
        """
        # Загрузка данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Обновление статуса второй книги
        Library.update_book_status(books[1]['id'], 'выдана')

        # Чтение обновленных данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            updated_books = json.load(f)

        # Проверка статуса второй книги
        self.assertEqual(updated_books[1]['status'], 'выдана')

    def test_delete_book(self):
        """
        Тестирование функции delete_book.

        Проверяет, что функция удаляет книгу по её ID из файла.
        """
        # Чтение данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Удаление книги по её ID
        Library.delete_book(books[0]['id'])

        # Чтение обновленных данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            updated_books = json.load(f)

        # Проверка количества книг
        self.assertEqual(len(updated_books), 3)

        # Проверка, что удалённая книга не осталась в списке
        self.assertNotEqual(updated_books[0]['title'], 'Цитадель')
        
    def test_delete_nonexistent_book(self):
        """
        Тестирование функции delete_book.

        Проверяет, что функция не удаляет книгу по её ID, если она не существует.
        """
        # Чтение данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Удаление книги по её ID
        Library.delete_book('nonexistent_id')
        
        self.assertTrue("Книга с ID nonexistent_id не найдена.")

        # Чтение обновленных данных из файла
        with open(self.test_file, 'r', encoding='utf-8') as f:
            updated_books = json.load(f)

        # Проверка количества книг
        self.assertEqual(len(updated_books), 4)

if __name__ == '__main__':
    unittest.main()
