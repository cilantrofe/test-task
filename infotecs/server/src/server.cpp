#include "server.hpp"
#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

// Метод запускает сервер и начинает принимать соединения
void Server::run()
{
    // Создаем сокет для прослушивания подключений
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    int buffer;

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        std::cerr << "Socket failed" << std::endl;
        exit(EXIT_FAILURE);
    }

    // Устанавливаем опции сокета
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))
    {
        std::cerr << "setsockopt" << std::endl;
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Задаем адрес и порт для прослушивания
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
    {
        std::cerr << "Bind failed" << std::endl;
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Устанавливаем режим прослушивания
    if (listen(server_fd, 3) < 0)
    {
        std::cerr << "Listen" << std::endl;
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    while (true)
    {
        std::cout << "Waiting for connection..." << std::endl;

        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0)
        {
            std::cerr << "Accept" << std::endl;
            continue;
        }

        // Обрабатываем новое соединение
        processConnection(new_socket);
        close(new_socket);
    }

    close(server_fd);
}

// Метод обрабатывает новое соединение
// Читает данные с сокета, проверяет их на корректность и выводит результат
void Server::processConnection(int socket)
{
    // Читаем данные с сокета
    int buffer;
    read(socket, &buffer, sizeof(buffer));

    // Проверяем корректность данных
    if (buffer > 2 && buffer % 32 == 0)
    {
        std::cout << "Received valid data: " << buffer << std::endl;
    }
    else
    {
        std::cerr << "Error: Invalid data" << std::endl;
    }
}
