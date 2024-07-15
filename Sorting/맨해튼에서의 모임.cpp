#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N, M; // 점의 차원과 점의 개수

    std::cin >> N >> M;

    std::vector<long long> points[1000]; // 1000차원 벡터 형성
    std::vector<long long> result;       // 결과 벡터

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            long long point;
            std::cin >> point;             // 점 입력
            points[j].emplace_back(point); // j차원 벡터에 저장
        }
    }

    long long dist = 0;

    for (int i = 0; i < N; i++)
    {
        std::sort(points[i].begin(), points[i].end()); // 정렬
        result.emplace_back(points[i][M / 2]);
        for (auto &p : points[i])
        {
            dist += std::abs(p - result.back());
        }
    }

    std::cout << dist << "\n";
    for (auto &answer : result)
    {
        std::cout << answer << " ";
    }

    return 0;
}