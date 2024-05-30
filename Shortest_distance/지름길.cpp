#include <iostream>
#include <queue>
#include <utility>    // for std::pair
#include <functional> // for std::greater

#define INF 987654321

using namespace std;

void dijkstra(int start, vector<int>& distance, vector<vector<pair<int, int>>>& graph)
{
    // pair�� ����ϴ� ���������� �켱���� ť ����
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({ start, 0 }); // ���۰� �Ÿ� �Է�
    distance[start] = 0; // �Ÿ��� 0

    // �� �� ���� �ݺ�
    while (!pq.empty())
    {
        int curr = pq.top().first;
        int dist = pq.top().second;
        pq.pop(); // ������

        if (dist > distance[curr])
            continue;

        for (const auto& node : graph[curr])
        {
            int next = node.first;    // ���� ���
            int weight = node.second; // ���� ����� �Ÿ�
            int cost = dist + weight; // ������� �Ÿ� + ���� ��� �Ÿ�

            if (cost < distance[next]) // ���� �Ÿ��� �۴ٸ�
            {
                distance[next] = cost; // ����
                pq.push({ next, cost }); // �켱���� ť �߰�
            }
        }
    }
}

int main()
{
    int n; // �������� ����
    int d; // ��ӵ��� �Ÿ�

    cin >> n >> d;

    vector<int> distance(d + 1, INF);

    vector<vector<pair<int, int>>> graph(d + 1);

    for (int i = 0; i < d; i++)
    {
        graph[i].emplace_back(i + 1, 1); // ���� ��� ����
    }

    for (int i = 0; i < n; i++)
    {
        int start, end, shortcut;
        // ����, ��, ������ ���� �Է�
        cin >> start >> end >> shortcut;

        // ���� �Ѿ�ٸ�
        if (d < end)
            continue;

        graph[start].emplace_back(end, shortcut);
    }

    dijkstra(0, distance, graph);
    cout << distance[d];
}