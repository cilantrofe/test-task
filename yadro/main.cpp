#include "computer_club.hpp"

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
        exit(1);
    }

    std::ifstream in(argv[1]);
    if (!in.is_open())
    {
        std::cerr << "Error opening file " << argv[1] << std::endl;
        exit(1);
    }

    std::string line;

    if (in.is_open())
    {
        int numbers, price;
        std::string open_time, close_time;

        if (!(in >> numbers >> open_time >> close_time >> price >> std::ws))
        {
            std::cerr << "Invalid input format." << std::endl;
            exit(1);
        }

        if (numbers <= 0 || price <= 0)
        {
            std::cerr << "Number of tables and price must be positive integers." << std::endl;
            exit(1);
            ;
        }

        std::regex time_format("\\d{2}:\\d{2} \\d{2}:\\d{2}");
        if (!std::regex_match(open_time + " " + close_time, time_format))
        {
            std::cerr << "Expected time format HH:MM HH:MM." << std::endl;
            return 1;
        }

        std::cout << open_time << '\n';

        ComputerClub club(numbers, open_time, close_time, price);

        while (std::getline(in, line))
        {
            club.event_handling(line);
        }

        club.print_last_clients();

        std::cout << close_time << '\n';

        club.print_tables();
    }

    in.close();

    return 0;
}
