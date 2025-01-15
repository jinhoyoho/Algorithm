#include <iostream>
#include <vector>
#include <string>

int checkSame(int x, int y, int N, std::vector<std::vector<int>> matrix)
{
    int basis = matrix[x][y];

    for (int i = x; i < x + N; i++)
    {
        for (int j = y; j < y + N; j++)
        {
            if (basis != matrix[i][j])
            {
                return -1; // different
            }
        }
    }

    return basis; // all same (0 or 1)
}

void recursive(int x, int y, int N, std::vector<std::vector<int>> matrix)
{
    int flag = checkSame(x, y, N, matrix); // check same

    if (flag != -1)
    {
        std::cout << flag;
    }
    else // not same with others
    {
        std::cout << "(";
        recursive(x, y, N / 2, matrix);                 // left up
        recursive(x, y + N / 2, N / 2, matrix);         // right up
        recursive(x + N / 2, y, N / 2, matrix);         // left down
        recursive(x + N / 2, y + N / 2, N / 2, matrix); // right down
        std::cout << ")";
    }
}

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N;                                                        // size of video
    std::cin >> N;                                                // input N
    std::vector<std::vector<int>> matrix(N, std::vector<int>(N)); // NxN matrix

    for (int i = 0; i < N; i++)
    {
        std::string line;
        std::cin >> line; // input an one line

        for (int j = 0; j < N; j++)
        {
            matrix[i][j] = line[j] - '0'; // string to number
        }
    }

    recursive(0, 0, N, matrix); // recursive

    return 0;
}