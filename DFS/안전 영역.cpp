#include <iostream>
#include <vector>

using namespace std;

int n; // 행과 열의 개수

bool dfs(int x, int y, vector<vector<int>>& visited)
{
    if (x < 0 || x >= n || y < 0 || y >= n)
    {
        return false;
    }

    if (visited[x][y] == 0) // 방문하지 않았다면
    {
        visited[x][y] = 1; // 방문 처리

        dfs(x + 1, y, visited);
        dfs(x - 1, y, visited);
        dfs(x, y - 1, visited);
        dfs(x, y + 1, visited); // 상하좌우

        return true;
    }
    return false;
}

int main(void)
{
    int result = 0;     // 결과
    int max_height = 0; // 높이 1이상 100이하의 정수
    cin >> n;           // 입력

    // n칸 만들고, 그 안을 vector<int>(5,0)으로 채운다.
    // vector를 n칸 만들고, 그 안을 0으로 채운다.
    vector<vector<int>> graph(n, vector<int>(n, 0)); // 그래프

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
            max_height = max(max_height, graph[i][j]); // 가장 높은 높이 구하기
        }
    }

    for (int i = 0; i <= max_height; i++)
    {
        vector<vector<int>> visited(n, vector<int>(n, 0)); // 방문 여부 (계속 초기화)
        int count = 0;                                     // 안전 구역 개수

        // 모든 구역 탐색
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (graph[j][k] <= i) // 비가 많이 왔다면
                {
                    visited[j][k] = 1; // 침수
                }
            }
        }

        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (dfs(j, k, visited) == true)
                {
                    count += 1;
                }
            }
        }

        result = max(result, count);
    }

    cout << result; // 결과 출력

    return 0;
}