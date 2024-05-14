#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int n; // 행과 열의 개수

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

void bfs(int x, int y, int height, vector<vector<bool>>& visited, vector<vector<int>> graph)
{
    queue<pair<int, int>> Q;
    Q.push(make_pair(x, y));
    visited[x][y] = true;

    while (!Q.empty())
    {
        pair<int, int> cur = Q.front(); // 현재 좌표 추출
        Q.pop();                        // 좌표 없애기

        for (int i = 0; i < 4; i++)
        {
            int next_x = cur.first + dx[i];
            int next_y = cur.second + dy[i];

            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= n)
            {
                continue; // return으로 작성시, 함수가 종료되므로 오류
            }

            if (!visited[next_x][next_y] && graph[next_x][next_y] > height)
            {
                Q.push(make_pair(next_x, next_y));
                visited[next_x][next_y] = true;
            }
        }
    }
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
        vector<vector<bool>> visited(n, vector<bool>(n, false)); // 방문 여부 (계속 초기화)
        int count = 0;                                           // 안전 구역 개수

        // 모든 구역 탐색
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (!visited[j][k] && graph[j][k] > i) // 방문하지 않고 침수되지 않았다면
                {
                    bfs(j, k, i, visited, graph); //  위치와 높이 전달
                    count += 1;
                }
            }
        }

        result = max(result, count);
    }

    cout << result; // 결과 출력

    return 0;
}