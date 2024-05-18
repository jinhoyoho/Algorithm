#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int dx[4] = { 0, -1, 0, 1 };
int dy[4] = { 1, 0, -1, 0 };

int n; // 가로, 세로 크기

int bfs(int x, int y, vector<vector<bool>>& visited, vector<vector<int>>& graph)
{
    int house = 1;        //  집 하나부터 시작
    visited[x][y] = true; // 방문 기록

    queue<pair<int, int>> q; // 큐
    q.push(make_pair(x, y)); // 대입

    while (!q.empty())
    {
        int cur_x = q.front().first;  // x 좌표
        int cur_y = q.front().second; // y 좌표
        q.pop();                      //  큐에서 빼기

        for (int i = 0; i < 4; i++)
        {
            int new_x = cur_x + dx[i];
            int new_y = cur_y + dy[i]; //  새로 이동할 좌표 저장

            if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= n) // 범위 밖이라면
                continue;

            if (!visited[new_x][new_y] && graph[new_x][new_y] == 1) //  방문하지 않았다면
            {
                visited[new_x][new_y] = true;    //  방문 표시
                house++;                         // 집 개수 증가
                q.push(make_pair(new_x, new_y)); // 큐에 저장
            }
        }
    }

    return house;
}

int main()
{
    int country = 0; // 마을 개수

    cin >> n; // 입력

    // 결과를 저장할 우선순위 큐, 오름차순으로 정렬
    priority_queue<int, vector<int>, greater<int>> result;

    vector<vector<int>> graph(n, vector<int>(n, 0));         // graph 생성
    vector<vector<bool>> visited(n, vector<bool>(n, false)); // visited 생성

    cin.ignore(); // cin과 getline 사이에 버퍼를 비워주는 역할

    for (int i = 0; i < n; i++)
    {
        string line; //  한 줄씩 입력
        cin >> line;
        for (int j = 0; j < n; j++)
        {
            graph[i][j] = line[j] - '0'; // 아스키코드 고려하여 0 빼주기
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j] && graph[i][j] == 1) // 방문한 적이 없고 집이 존재하다면
            {
                country++;
                int house = 0;                     //  마을 개수 +1
                house = bfs(i, j, visited, graph); // bfs 실행
                result.push(house);                // 결과 저장
            }
        }
    }

    cout << country << "\n"; // 마을 개수 출력

    while (!result.empty())
    {
        cout << result.top() << "\n"; // 출력
        result.pop();                 // 제거
    }
}