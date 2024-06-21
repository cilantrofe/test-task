#include <iostream>
#include <cmath>

class Shape
{
public:
    virtual void draw() const = 0;
    virtual ~Shape() {}
};

class Circle : public Shape
{
public:
    Circle(double r) : radius(r) {}

    void draw() const override
    {
        const int size = 2 * radius + 1;
        for (int y = 0; y < size; ++y)
        {
            for (int x = 0; x < size; ++x)
            {
                if (sqrt((x - radius) * (x - radius) + (y - radius) * (y - radius)) < radius)
                {
                    std::cout << "*";
                }
                else
                {
                    std::cout << " ";
                }
            }
            std::cout << '\n';
        }
    }

private:
    double radius;
};

class Triangle : public Shape
{
public:
    Triangle(double h) : height(h) {}

    void draw() const override
    {
        for (int i = 1; i <= height; ++i)
        {
            for (int j = 0; j < height - i; ++j)
            {
                std::cout << " ";
            }
            for (int j = 0; j < 2 * i - 1; ++j)
            {
                std::cout << "*";
            }
            std::cout << '\n';
        }
    }

private:
    double height;
};

class Rectangle : public Shape
{
public:
    Rectangle(double w, double h) : width(w), height(h) {}

    void draw() const override
    {
        for (int i = 0; i < height; ++i)
        {
            for (int j = 0; j < width; ++j)
            {
                std::cout << "*";
            }
            std::cout << '\n';
        }
    }

private:
    double width;
    double height;
};

class Square : public Rectangle
{
public:
    Square(double s) : Rectangle(s, s) {}
};

int main()
{
    Circle circle(5);

    Triangle triangle(4);
    Rectangle rectangle(6, 3);
    Square square(4);

    circle.draw();
    std::cout << '\n';

    triangle.draw();
    std::cout << '\n';

    rectangle.draw();
    std::cout << '\n';

    square.draw();
    std::cout << '\n';

    return 0;
}
