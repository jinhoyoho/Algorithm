#include <iostream>
#include <utility> // to use pair
#include <vector>  // to use vector
#include <algorithm>

// true: descending, false: ascending
bool cmp(std::pair<int, int> point1, std::pair<int, int> point2)
{
    if (point1.second > point2.second) // point1 is bigger than point2
        return false;
    else if (point1.second == point2.second && point1.first > point2.first) // point1 is bigger than point2
        return false;
    else // point2 is bigger than point1
        return true;
}

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N; // number of points

    std::cin >> N;

    std::vector<std::pair<int, int>> points(N); // point array or Nx2 matrix

    for (int i = 0; i < N; i++)
    {
        std::cin >> points[i].first >> points[i].second;
    }

    std::sort(points.begin(), points.end(), cmp);

    for (int i = 0; i < N; i++)
    {
        std::cout << points[i].first << " " << points[i].second << "\n";
    }

    return 0;
}