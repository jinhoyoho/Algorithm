#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    std::string str;

    char vowel_array[10] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

    while (std::getline(std::cin, str))
    {
        std::vector<std::string> my_str;
        std::string temp;

        for (int i = 0; i < str.size(); i++)
        {
            if (str[i] != ' ') // 공백이 아닌 경우
            {
                temp += str[i];
            }
            else
            {
                my_str.push_back(temp);
                temp = "";
            }
        }

        my_str.push_back(temp); // 마지막 단어 저장

        std::vector<std::string> vowel;
        std::vector<std::string> result;

        for (int i = 0; i < my_str.size(); i++)
        {
            if (my_str[i][0] == 'a' || my_str[i][0] == 'e' || my_str[i][0] == 'i' || my_str[i][0] == 'o' || my_str[i][0] == 'u' || my_str[i][0] == 'A' || my_str[i][0] == 'E' || my_str[i][0] == 'I' || my_str[i][0] == 'O' || my_str[i][0] == 'U')
            {
                vowel.push_back(my_str[i]);
            }
        }

        std::reverse(vowel.begin(), vowel.end()); // 뒤집기

        int idx = 0;

        for (int i = 0; i < my_str.size(); i++)
        {
            if (my_str[i][0] == 'a' || my_str[i][0] == 'e' || my_str[i][0] == 'i' || my_str[i][0] == 'o' || my_str[i][0] == 'u' || my_str[i][0] == 'A' || my_str[i][0] == 'E' || my_str[i][0] == 'I' || my_str[i][0] == 'O' || my_str[i][0] == 'U')
            {
                my_str[i] = vowel[idx];
                idx++;
            }
        }

        for (int i = 0; i < my_str.size(); i++)
        {
            std::cout << my_str[i] << " ";
        }
    }

    return 0;
}