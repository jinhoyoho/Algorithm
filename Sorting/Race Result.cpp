#include <iostream>
#include <vector>
#include <algorithm>

bool cmp(std::vector<int> &v1, std::vector<int> &v2)
{
    if (v1[0] == v2[0])
    {
        if (v1[1] == v2[1])
        {
            return v1[2] < v2[2];
        }
        else
        {
            return v1[1] < v2[1];
        }
    }
    else
    {
        return v1[0] < v2[0];
    }
}

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N;
    std::cin >> N;

    std::vector<std::vector<int>> arr(N, std::vector<int>(3));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            std::cin >> arr[i][j];
        }
    }

    std::sort(arr.begin(), arr.end(), cmp);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            std::cout << arr[i][j] << " ";
        }
        std::cout << "\n";
    }
}