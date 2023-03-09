#include <vector>
#include <iostream>

int accessElement(int length2, int i, int j, int k)
{
    return ((length2 + 1)*i + j)*2 + k;
}

int main()
{
    std::vector<int> sequence1(1000);
    std::vector<int> sequence2(1000);

    std::vector<int> solution(2004002);

    int length1, length2;

    std::cin >> length1;
    for(int index = 0; index < length1; index++)
        std::cin >> sequence1[index];
    
    std::cin >> length2;
    for(int index = 0; index < length2; index++)
        std::cin >> sequence2[index];
    
    for(int index1 = 0; index1 < length1; index1++)
        for(int index2 = 0; index2 < length2; index2++)
        { 
            int& clength = solution[accessElement(length2, index1 + 1, index2 + 1, 0)];
            int& cdir = solution[accessElement(length2, index1 + 1, index2 + 1, 1)];

            if(sequence1[index1] == sequence2[index2])
                {
                    clength = solution[accessElement(length2, index1, index2, 0)] + 1;
                    cdir = 3;
                }
            else
                {
                    int up = solution[accessElement(length2, index1, index2 + 1, 0)];
                    int left = solution[accessElement(length2, index1 + 1, index2, 0)];

                    if(up >= left)
                    {
                        clength = up;
                        cdir = 1;
                    }
                    else
                    {
                        clength = left;
                        cdir = 2;
                    }
                }

        }

    // for(int i = 0; i < length1 + 1; i++)
    //     {
    //     for(int j = 0; j < length2 + 1; j++)
    //             std::cout << "(" << i << "," << j << "): " << solution[accessElement(length2, i, j, 0)] << "," << solution[accessElement(length2, i, j, 1)] << "  ";
    //         std::cout << std::endl;
    //     }

    int index1, index2, direction;
    
    index1 = length1;
    index2 = length2;
    direction = 4;

    std::vector<int> result;

    while(direction != 0)
    {
        direction = solution[accessElement(length2, index1, index2, 1)];

        // std::cout << index1 << " " << index2 << ": " << direction << std::endl;

        switch (direction)
        {
        case 1:
            index1 -= 1;
            break;
        
        case 2:
            index2 -= 1;
            break;

        case 3:
            result.push_back(sequence1[index1 - 1]);
            index1 -= 1;
            index2 -= 1;
            break;
        }
    }
    
    for(int index = result.size() - 1; index >= 0; index--)
    {
        std::cout << result[index];
        if(index != 0) std::cout << " ";
    }
    std::cout << std::endl;
}