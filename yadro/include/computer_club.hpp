#ifndef COMPUTER_CLUB_HPP
#define COMPUTER_CLUB_HPP

#include <string>
#include <sstream>
#include <ctime>
#include <iostream>
#include <fstream>
#include <map>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <vector>
#include <cstdio>
#include <regex>

#define CLIENT_ARRIVE 1
#define CLIENT_SEAT 2
#define CLIENT_WAIT 3
#define CLIENT_LEFT 4

#define OUT_CLIENT_LEFT 11
#define OUT_CLIENT_QUEUE_SEAT 12
#define OUT_ERROR 13

struct Table
{
    int minutes = 0; // Время работы стола в минутах
    int money = 0;   // Выручка
};

struct Client
{
    std::tm time = {}; // Когда сел за стол
    int table = 0;     // Номер стола
};

class ComputerClub
{
public:
    ComputerClub(const int &numbers, const std::string &open_time, const std::string &close_time, const int &price);

    // Обработчик событий
    void event_handling(const std::string &str);

    // Последние клиенты
    void print_last_clients();

    // Информация о столах в конце рабочего дня
    void print_tables() const;

private:
    // Перевод в минуты
    static int to_minutes(const std::tm &tm);

    // Форматирование минут
    static std::string format_minutes(const int &min);

    // Парсинг строки
    static std::tm parse_time(const std::string &time);

    // Вычисление выручки, округление
    int calculate_money(const int &time) const;

    // Проверка на рабочие часы
    bool is_working_hours(const tm &current_time) const;

private:
    int numbers_;        // Число столов
    std::tm open_time_;  // Время открытия
    std::tm close_time_; // Время закрытия
    int price_;          // Цена за час

    // Использую unordered_map, так как часто обращаюсь по ключу / вставляю, а в данной структуре это O(1) в среднем
    // Не очень, что две мапы, но тут нужно и стол - клиент, и клиент - стол, это какой-нибудь Bimap из Boost,
    // но это , наверное, только усложняет, да и задачка тестовая и так быстрее всего будет
    std::unordered_map<std::string, Client> clients_times_; // Имя клиента : время входа, номер стола
    std::unordered_map<int, std::string> tables_client_;    // Номер стола : имя клиента (столы, которые работают)
    std::queue<std::string> clients_queue_;                 // Очередь клиентов
    std::vector<Table> tables_inf_;                         // Время проведенное за столом и выручка
};

#endif // COMPUTER_CLUB_HPP
