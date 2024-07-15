#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N; // 정수 개수
    std::cin >> N;

    float real = 0;
    float imag = 0;

    for (int i = 0; i < N; i++)
    {
        long long A;
        std::cin >> A;

        if (A % 3 == 0)
            real += 1;
        else if (A % 3 == 1)
            imag += 1;
        else if (A % 3 == 2)
        {
            real -= 1;
            imag -= 1;
        }
    }

    std::cout << imag << " " << real;
}