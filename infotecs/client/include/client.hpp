#ifndef CLIENT_H
#define CLIENT_H

#include <string>
#include <thread>
#include <mutex>
#include <condition_variable>

// Класс для клиента, который отправляет данные на сервер и ждет, пока сервер обработает данные.
class Client
{
public:
    // Конструктор клиента.
    Client();

    // Запускает потоки ввода и обработки данных.
    void run();

private:
    // Потoк для приема данных от пользователя.
    void inputThread();

    // Потoк для отправки данных на сервер.
    void processThread();

    //  Проверяет, является ли входной строка корректной (состоит только из цифр и не длиннее 64 символов).
    bool isValidInput(const std::string &input);

    // Обрабатывает входную строку, сортирует ее по убыванию, заменяет все четные цифры на 'K'.
    std::string processInput(const std::string &input);

    // Мьютекс для синхронизации доступа к буферу данных.
    std::mutex mtx;

    // Семафор для ожидания готовности данных в буфере.
    std::condition_variable cv;

    // Флаг, указывающий, что данные готовы для отправки на сервер.
    bool data_ready;

    // Буфер для хранения данных, готовых к отправке на сервер.
    std::string buffer;
};

#endif // CLIENT_H
