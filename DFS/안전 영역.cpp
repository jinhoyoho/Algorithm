#include <iostream>
#include <vector>

using namespace std;

int n; // ��� ���� ����

bool dfs(int x, int y, vector<vector<int>>& visited)
{
    if (x < 0 || x >= n || y < 0 || y >= n)
    {
        return false;
    }

    if (visited[x][y] == 0) // �湮���� �ʾҴٸ�
    {
        visited[x][y] = 1; // �湮 ó��

        dfs(x + 1, y, visited);
        dfs(x - 1, y, visited);
        dfs(x, y - 1, visited);
        dfs(x, y + 1, visited); // �����¿�

        return true;
    }
    return false;
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
        vector<vector<int>> visited(n, vector<int>(n, 0)); // �湮 ���� (��� �ʱ�ȭ)
        int count = 0;                                     // ���� ���� ����

        // ��� ���� Ž��
        for (int j = 0; j < n; j++)
        {
            for (int k = 0; k < n; k++)
            {
                if (graph[j][k] <= i) // �� ���� �Դٸ�
                {
                    visited[j][k] = 1; // ħ��
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

    cout << result; // ��� ���

    return 0;
}