#include <iostream>
#include <ctime>
#include <cstdio>

int main()
{
    time_t timer;
    struct tm *t;
    timer = time(NULL);

    t = localtime(&timer);

    std::cout << t->tm_year + 1900 << '-';
    std::cout.width(2);
    std::cout.fill('0');
    std::cout << t->tm_mon + 1 << '-';
    std::cout.width(2);
    std::cout.fill('0');
    std::cout << t->tm_mday;
}