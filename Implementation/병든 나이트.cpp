#include <iostream>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    int N, M; // 체스판 세로, 가로
    std::cin >> N >> M;

    int result = 1; // 이동한 판의 개수

    if ((N >= 3) && (M >= 7)) // 체스판이 커서 4가지 모두 이동
    {
        result += M - 7 + 4; // (7,1)부터 시작하며 4번을 이동함
    }
    else if (N == 2) // 1번과 4번은 이동 못함
    {
        M -= 1;
        result += M / 2; // 2, 3번만 이용
        if (result > 4)  // 4가지 이동을 모두 갈 수 없으므로 4까지밖에 안됨
            result = 4;
    }
    else if (N == 1)
    {
        result = 1; // 이동 x
    }
    else
    {
        result += M - 1; // 1, 4번을 이용해서 이동
        if (result > 4)  // 4가지 이동을 모두 갈 수 없으므로 4까지밖에 안됨
            result = 4;
    }

    std::cout << result;
}