#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n; // 배열의 개수
    string str, tempString;

    cin >> n;
    cin >> str;

    int result = 0;

    for (int i = 0; i < n; i++)
    {
        tempString = str[i]; // stoi 사용을 위해서 String으로 변경
        result += stoi(tempString);
    }

    cout << result;
}