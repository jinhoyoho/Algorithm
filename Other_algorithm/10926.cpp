#include <iostream>
#include <string>

int main()
{
    std::string name;

    // std::cin >> name;
    // cin.ignore();

    // char nameArray[100];
    // std::cin.getline(nameArray, 100);

    std::getline(std::cin, name);

    std::cout << name << "??!";
    
    return 0;
}