#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool cmp(vector<int> &v1, vector<int> &v2)
{
    if (v1[1] == v2[1])
    {                         // 뒤에 것 기준으로 같다면
        return v1[0] < v2[0]; // 앞에 것이 큰 것
    }
    else
    {
        return v1[1] < v2[1]; // 뒤에가 더 크면 1, 작으면 0
    }
}

int main()
{
    int count;
    cin >> count;

    vector<vector<int>> conference(count, vector<int>(2, 0));

    for (int i = 0; i < count; i++)
    {
        int start, end;
        cin >> start >> end;
        conference[i][0] = start;
        conference[i][1] = end;
    }

    sort(conference.begin(), conference.end());      // 시작 시간 정렬
    sort(conference.begin(), conference.end(), cmp); // 종료 시간 정렬

    int result = 0; // 결과
    int end = 0;    // 시간

    for (int i = 0; i < count; i++)
    {
        if (conference[i][0] >= end)
        {
            result += 1;
            end = conference[i][1];
        }
    }

    cout << result << endl;

    return 0;
}