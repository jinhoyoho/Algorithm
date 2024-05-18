#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int dx[4] = { 0, -1, 0, 1 };
int dy[4] = { 1, 0, -1, 0 };

int n; // ����, ���� ũ��

int bfs(int x, int y, vector<vector<bool>>& visited, vector<vector<int>>& graph)
{
    int house = 1;        //  �� �ϳ����� ����
    visited[x][y] = true; // �湮 ���

    queue<pair<int, int>> q; // ť
    q.push(make_pair(x, y)); // ����

    while (!q.empty())
    {
        int cur_x = q.front().first;  // x ��ǥ
        int cur_y = q.front().second; // y ��ǥ
        q.pop();                      //  ť���� ����

        for (int i = 0; i < 4; i++)
        {
            int new_x = cur_x + dx[i];
            int new_y = cur_y + dy[i]; //  ���� �̵��� ��ǥ ����

            if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= n) // ���� ���̶��
                continue;

            if (!visited[new_x][new_y] && graph[new_x][new_y] == 1) //  �湮���� �ʾҴٸ�
            {
                visited[new_x][new_y] = true;    //  �湮 ǥ��
                house++;                         // �� ���� ����
                q.push(make_pair(new_x, new_y)); // ť�� ����
            }
        }
    }

    return house;
}

int main()
{
    int country = 0; // ���� ����

    cin >> n; // �Է�

    // ����� ������ �켱���� ť, ������������ ����
    priority_queue<int, vector<int>, greater<int>> result;

    vector<vector<int>> graph(n, vector<int>(n, 0));         // graph ����
    vector<vector<bool>> visited(n, vector<bool>(n, false)); // visited ����

    cin.ignore(); // cin�� getline ���̿� ���۸� ����ִ� ����

    for (int i = 0; i < n; i++)
    {
        string line; //  �� �پ� �Է�
        cin >> line;
        for (int j = 0; j < n; j++)
        {
            graph[i][j] = line[j] - '0'; // �ƽ�Ű�ڵ� ����Ͽ� 0 ���ֱ�
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j] && graph[i][j] == 1) // �湮�� ���� ���� ���� �����ϴٸ�
            {
                country++;
                int house = 0;                     //  ���� ���� +1
                house = bfs(i, j, visited, graph); // bfs ����
                result.push(house);                // ��� ����
            }
        }
    }

    cout << country << "\n"; // ���� ���� ���

    while (!result.empty())
    {
        cout << result.top() << "\n"; // ���
        result.pop();                 // ����
    }
}