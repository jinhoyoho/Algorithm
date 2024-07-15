#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int T; // test case
    std::cin >> T;

    for (int i = 0; i < T; i++)
    {
        long long n, m; // 체력과 먹이
        std::cin >> n >> m;

        long long day = 1; // 살아있는 날짜

        while (n > 1) //   1이 될때까지 나누기
        {
            n /= 2;
            day++;
        }
        day += m;

        std::cout << day << "\n";
    }
}