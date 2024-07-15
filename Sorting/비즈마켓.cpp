#include <iostream>
#include <queue>
#include <functional>
#include <vector>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    long long N, M;
    long long cust_satis = 0;

    std::cin >> N >> M;

    std::priority_queue<long long> satis;                                                 // 큰 것 부터 저장
    std::priority_queue<long long, std::vector<long long>, std::greater<long long>> cost; // 작은 것 부터 저장

    for (int i = 0; i < N; i++)
    {
        long long value;
        std::cin >> value;
        satis.push(value);
    }

    for (int i = 0; i < M; i++)
    {
        long long value;
        std::cin >> value;
        cost.push(value);
    }

    while (true)
    {
        if (cost.empty() || satis.empty())
            break;

        long long A = satis.top();
        satis.pop();
        long long B = cost.top();
        cost.pop();

        if (A < B)
            break;

        cust_satis += A - B;
    }

    std::cout << cust_satis;

    return 0;
}