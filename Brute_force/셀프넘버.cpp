#include <iostream>

#define NUMBER 10001

int selfNumber(bool array[], int index)
{
    int sum = index; // sum

    do
    {
        sum += index % 10; // sum last digit
        index /= 10;       // divide 10

    } while (index != 0);

    return sum;
}

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    bool array[NUMBER];

    // memset(array, true, sizeof(bool) * 10001);
    std::fill_n(array, NUMBER, true); // set array all true

    // check array is selfNumber
    for (int i = 1; i < NUMBER; i++)
    {
        int num = selfNumber(array, i);
        if (num < NUMBER) // num must be smaller than NUMBER
            array[num] = false;
    }

    // print array
    for (int i = 1; i < NUMBER; i++)
    {
        if (array[i] == true)
        {
            std::cout << i << "\n";
        }
    }

    return 0;
}