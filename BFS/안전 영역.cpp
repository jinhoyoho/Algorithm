#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int n; // ��� ���� ����

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, 1, 0, -1 };

void bfs(int x, int y, int height, vector<vector<bool>>& visited, vector<vector<int>> graph)
{
    queue<pair<int, int>> Q;
    Q.push(make_pair(x, y));
    visited[x][y] = true;

    while (!Q.empty())
    {
        pair<int, int> cur = Q.front(); // ���� ��ǥ ����
        Q.pop();                        // ��ǥ ���ֱ�

        for (int i = 0; i < 4; i++)
        {
            int next_x = cur.first + dx[i];
            int next_y = cur.second + dy[i];

            if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= n)
            {
                continue; // return���� �ۼ���, �Լ��� ����ǹǷ� ����
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
    int result = 0;     // ���
    int max_height = 0; // ���� 1�̻� 100������ ����
    cin >> n;           // �Է�

    // nĭ �����, �� ���� vector<int>(5,0)���� ä���.
    // vector�� nĭ �����, �� ���� 0���� ä���.
    vector<vector<int>> graph(n, vector<int>(n, 0)); // �׷���

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> graph[i][j];
            max_height = max(max_height, graph[i][j]); // ���� ���� ���� ���ϱ�
        }
    }

    for (int i = 0; i <= max_height; i++)
    {
        vector<vector<bool>> visited(n, vector<bool>(n, false)); // �湮 ���� (��� �ʱ�ȭ)
        int count = 0;                                           // ���� ���� ����

        // ��� ���� Ž��
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (!visited[j][k] && graph[j][k] > i) // �湮���� �ʰ� ħ������ �ʾҴٸ�
                {
                    bfs(j, k, i, visited, graph); //  ��ġ�� ���� ����
                    count += 1;
                }
            }
        }

        result = max(result, count);
    }

    cout << result; // ��� ���

    return 0;
}