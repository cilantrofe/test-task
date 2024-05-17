#include "computer_club.hpp"

ComputerClub::ComputerClub(const int &numbers, const std::string &open_time, const std::string &close_time, const int &price)
    : numbers_(numbers),
      open_time_(parse_time(open_time)),
      close_time_(parse_time(close_time)),
      price_(price),
      tables_inf_(numbers)
{
}

// Обработчик событий
void ComputerClub::event_handling(const std::string &str)
{
    // Проверка на формат
    std::regex event_format(R"(\d{2}:\d{2} \d [a-z0-9_\\-]+(?: \d+)?[\s\S]?)");
    if (!std::regex_match(str, event_format))
    {
        std::cout << str << std::endl;
        std::cerr << "Invalid event format." << std::endl;
        exit(1);
    }

    std::tm tm_client = {0};
    int id, table = 0;
    char name[100]; // Предполагается, что имя не больше 100 символов

    std::sscanf(str.c_str(), "%d:%d %d %s %d", &tm_client.tm_hour, &tm_client.tm_min, &id, name, &table);

    if (!table && table > numbers_)
    {
        std::cout << str << std::endl;
        std::cerr << "Invalid table." << std::endl;
        exit(1);
    }

    // Время, чтобы удобно печатать в дальнейшем
    std::string time = str.substr(0, 5);

    // Печатаю входящее событие
    std::cout << str << std::endl;

    // Клиент пришел
    if (id == CLIENT_ARRIVE)
    {
        // Рабочие ли часы
        if (!is_working_hours(tm_client))
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "NotOpenYet");
        }
        // Уже в компьтерном клубе
        else if (clients_times_.find(name) != clients_times_.end())
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "YouShallNotPass");
        }
        // Добавляем в клуб
        else
        {
            clients_times_.emplace(name, Client());
        }
    }
    // Клиент сел за стол
    if (id == CLIENT_SEAT)
    {
        // Клиент не компьютерном клубе
        if (clients_times_.find(name) == clients_times_.end())
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "ClientUnknown");
        }
        // Такой стол уже занят
        else if (tables_client_.find(table) != tables_client_.end())
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "PlaceIsBusy");
        }
        else
        {
            tables_client_[table] = name; // Клиент занимает стол

            clients_times_[name].time = tm_client; // Запоминаем во сколько сел за стол
            clients_times_[name].table = table;    // Запоминаем какой стол
        }
    }
    // Клиент ждет
    if (id == CLIENT_WAIT)
    {
        // Есть свободные столы
        if (tables_client_.size() < numbers_)
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "ICanWaitNoLonger!");
        }
        // Очередь больше, чем столов
        else if (clients_queue_.size() > numbers_)
        {
            clients_times_.erase(name);
            printf("%s %d %s\n", time.c_str(), OUT_CLIENT_LEFT, name);
        }
        else
        {
            // Добавляем в очередь
            clients_queue_.push(name);
        }
    }
    // Клиент ушел
    if (id == CLIENT_LEFT)
    {
        // Клиент не компьютерном клубе
        if (clients_times_.find(name) == clients_times_.end())
        {
            printf("%s %d %s\n", time.c_str(), OUT_ERROR, "ClientUnknowsn");
        }
        else
        {
            // Во сколько ушёл
            int time = to_minutes(tm_client) - to_minutes(clients_times_[name].time);

            // Записываем время работы стола
            tables_inf_[clients_times_[name].table - 1].minutes += time;
            // Заранее считаем выручку, так как общее время работы стола не дает корректно посчитать выручку
            // - все таки разные клиенты и округление у каждого
            tables_inf_[clients_times_[name].table - 1].money += calculate_money(time);

            // Ждет ли кто-то
            if (!clients_queue_.empty())
            {
                // Первый в очереди занимает стол
                tables_client_.emplace(clients_times_[name].table, clients_queue_.front());

                printf("%s %d %s %d\n", str.substr(0, 5).c_str(), OUT_CLIENT_QUEUE_SEAT, clients_queue_.front().c_str(), clients_times_[name].table);

                // Обновляем информацию о клиенте, который только что сел за стол
                clients_times_[clients_queue_.front()].time = tm_client;
                clients_times_[clients_queue_.front()].table = clients_times_[name].table;
                // Удаляем из очереди
                clients_queue_.pop();
            }
            else
            {
                // Никого в очереди - стол свободен
                tables_client_.erase(clients_times_[name].table);
            }

            // Удаляем ушедшего клиента из компьютерного клуба
            clients_times_.erase(name);
        }
    }
}

// Последние клиенты
void ComputerClub::print_last_clients()
{
    // Сортируем по имени
    std::map<std::string, Client> clients_sorted(clients_times_.begin(), clients_times_.end());

    for (auto it = clients_sorted.begin(); it != clients_sorted.end(); ++it)
    {
        int time = to_minutes(close_time_) - to_minutes(it->second.time);

        if (it->second.table != 0)
        {
            tables_inf_[it->second.table - 1].minutes += time;
            tables_inf_[it->second.table - 1].money += calculate_money(time);
        }

        printf("%s %d %s\n", format_minutes(to_minutes(close_time_)).c_str(), OUT_CLIENT_LEFT, it->first.c_str());
    }
}

// Информация о столах в конце рабочего дня
void ComputerClub::print_tables() const
{
    for (std::size_t i = 0; i < tables_inf_.size(); i++)
    {
        printf("%ld %d %s\n", i + 1, tables_inf_[i].money, format_minutes(tables_inf_[i].minutes).c_str());
    }
}

// Перевод в минуты
int ComputerClub::to_minutes(const std::tm &tm)
{
    return tm.tm_hour * 60 + tm.tm_min;
}

// Форматирование минут
std::string ComputerClub::format_minutes(const int &min)
{
    int hours = min / 60;
    int minutes = min % 60;

    std::string res = "";

    if (hours < 10)
    {
        res += "0";
    }
    res += std::to_string(hours);
    res += ":";

    if (minutes < 10)
    {
        res += "0";
    }
    res += std::to_string(minutes);

    return res;
}

// Парсинг строки
std::tm ComputerClub::parse_time(const std::string &time)
{
    std::tm tm = {0};
    std::sscanf(time.c_str(), "%d:%d", &tm.tm_hour, &tm.tm_min);
    return tm;
}

// Вычисление выручки, округление
int ComputerClub::calculate_money(const int &time) const
{
    return std::ceil(time / 60.0) * price_;
}

// Проверка на рабочие часы
bool ComputerClub::is_working_hours(const tm &current_time) const
{
    return (to_minutes(current_time) >= to_minutes(open_time_) && to_minutes(current_time) <= to_minutes(close_time_));
}