#include <iostream>
#include <queue>
#include <utility>    // for std::pair
#include <functional> // for std::greater

#define INF 987654321

using namespace std;

void dijkstra(int start, vector<int>& distance, vector<vector<pair<int, int>>>& graph)
{
    // pair를 사용하는 오름차순의 우선순위 큐 정의
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({ start, 0 }); // 시작과 거리 입력
    distance[start] = 0; // 거리는 0

    // 빌 때 까지 반복
    while (!pq.empty())
    {
        int curr = pq.top().first;
        int dist = pq.top().second;
        pq.pop(); // 빼내기

        if (dist > distance[curr])
            continue;

        for (const auto& node : graph[curr])
        {
            int next = node.first;    // 다음 노드
            int weight = node.second; // 다음 노드의 거리
            int cost = dist + weight; // 현재까지 거리 + 다음 노드 거리

            if (cost < distance[next]) // 만약 거리가 작다면
            {
                distance[next] = cost; // 갱신
                pq.push({ next, cost }); // 우선순위 큐 추가
            }
        }
    }
}

int main()
{
    int n; // 지름길의 개수
    int d; // 고속도로 거리

    cin >> n >> d;

    vector<int> distance(d + 1, INF);

    vector<vector<pair<int, int>>> graph(d + 1);

    for (int i = 0; i < d; i++)
    {
        graph[i].emplace_back(i + 1, 1); // 다음 노드 연결
    }

    for (int i = 0; i < n; i++)
    {
        int start, end, shortcut;
        // 시작, 끝, 지름길 길이 입력
        cin >> start >> end >> shortcut;

        // 만약 넘어간다면
        if (d < end)
            continue;

        graph[start].emplace_back(end, shortcut);
    }

    dijkstra(0, distance, graph);
    cout << distance[d];
}