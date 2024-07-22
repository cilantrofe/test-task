#include "client.hpp"
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

// Конструктор класса Client
Client::Client() : data_ready(false) {}

// Метод запускает два потока для ввода и обработки данных
void Client::run()
{
    // Поток для ввода данных
    std::thread t1(&Client::inputThread, this);

    // Поток для обработки данных
    std::thread t2(&Client::processThread, this);

    t1.join(); // Ожидаем окончания потока ввода
    t2.join(); // Ожидаем окончания потока обработки
}

// Метод ввода данных
void Client::inputThread()
{
    while (true)
    {
        std::string input;
        std::cout << "Enter a string (digits only, max 64 characters): ";
        std::getline(std::cin, input); // Ввод строки данных

        // Проверка на корректность введенных данных
        if (!isValidInput(input))
        {
            std::cout << "Invalid input. Try again." << '\n';
            continue;
        }

        std::string processed_input = processInput(input); // Обработка данных

        {
            std::lock_guard<std::mutex> lock(mtx); // Блокировка мьютекса
            buffer = processed_input;              // Запись обработанных данных в буфер
            data_ready = true;
        }

        cv.notify_one(); // Уведомление о готовности данных для обработки
    }
}

// Метод проверки корректности введенных данных
bool Client::isValidInput(const std::string &input)
{
    return input.length() <= 64 && std::all_of(input.begin(), input.end(), ::isdigit); // Проверка на корректность введенных данных
}

// Метод обработки данных
std::string Client::processInput(const std::string &input)
{
    std::string result = input;

    // Сортировка данных в обратном порядке
    std::sort(result.begin(), result.end(), std::greater<char>());
    std::string output;
    for (char c : result)
    {
        if ((c - '0') % 2 == 0)
        {
            output += "KB";
        }
        else
        {
            output += c;
        }
    }
    return output;
}

// Метод обработки данных в потоке
void Client::processThread()
{
    int sock = 0;                 // Сокет для связи с сервером
    struct sockaddr_in serv_addr; // структура адреса сервера

    while (true)
    {
        std::unique_lock<std::mutex> lock(mtx); // Блокировка мьютекса
        cv.wait(lock, [this]
                { return data_ready; }); // Ожидание готовности данных для обработки

        std::string data = buffer;
        buffer.clear();
        data_ready = false; // Сброс флага готовности данных для обработки
        lock.unlock();      // Разблокировка мьютекса

        std::cout << "Processed string: " << data << '\n';

        int sum = 0;
        for (char c : data)
        {
            if (isdigit(c))
            {
                sum += (c - '0');
            }
        }

        if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        { // Создание сокета
            std::cerr << "Socket creation error" << '\n';
            continue;
        }

        serv_addr.sin_family = AF_INET;   // Установка семейства адресов
        serv_addr.sin_port = htons(8080); // Установка порта сервера

        // Проверка адреса сервера
        if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0)
        {
            std::cerr << "Invalid address/ Address not supported" << '\n';
            close(sock);
            continue;
        }

        // Попытка подключения к серверу
        if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
        {
            std::cerr << "Connection Failed" << '\n';
            close(sock);
            continue;
        }

        send(sock, &sum, sizeof(sum), 0); // Отправка суммы четных цифр на сервер
        close(sock);                      // Закрытие сокета
    }
}
