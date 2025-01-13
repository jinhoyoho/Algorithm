#include <iostream>

#define QUARTER 25
#define DIME 10
#define NICKEL 5
#define PENNY 1

int main()
{
    int testCase;

    std::cin >> testCase;

    while(testCase > 0)
    {   // initialize count variable
        int quarterCount = 0;
        int dimeCount = 0;
        int nickelCount = 0;
        int pennyCount = 0;

        int change;

        std::cin >> change;     // input change

        // divide change -> greedy
        quarterCount = change / QUARTER;
        change = change % QUARTER;

        dimeCount = change / DIME;
        change = change % DIME;

        nickelCount = change / NICKEL;
        change = change % NICKEL;

        pennyCount = change / PENNY;

        std::cout << quarterCount << " " << dimeCount << " " << nickelCount << " " << pennyCount << "\n";    // print

        testCase--;
    }
}