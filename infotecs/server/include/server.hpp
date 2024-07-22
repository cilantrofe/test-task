#ifndef SERVER_H
#define SERVER_H

// Класс-сервер, который прослушивает соединения и обрабатывает их.
class Server
{
public:
    // Запускает сервер и начинает принимать соединения.
    void run();

private:
    // Обрабатывает новое соединение.
    void processConnection(int socket);
};

#endif // SERVER_H
