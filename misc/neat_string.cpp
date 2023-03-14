#include <string>
#include <set>
#include <iostream>

int main()
{
    int swapsAvailable;
    std::cin >> swapsAvailable;

    std::string line;
    std::cin >> line;

    int totalLength = line.size();
    std::set<char> characters;

    int maxLength = 0;

    for (char c : line)
        characters.insert(c);

    for (char character : characters)
    {
        int start = 0, end = 0, length = 0, swaps = swapsAvailable;

        // std::cout << "phase 1 (" << character << ")\n" << std::endl;
        while (swaps > 0 && end < totalLength)
        {
            end++, length++;
            if (line[end-1] != character) swaps--;
            // std::cout << "end: " << end << " length: " << length << std::endl;
        }

        // std::cout << "phase 2\n" << std::endl;
        while(end < totalLength)
        {
            end++;
            // std::cout << "end: " << end << std::endl;
            if (line[end-1] != character)
            {   
                // std::cout << "foreign character" << std::endl;
                if(maxLength < length) maxLength = length;

                do
                start++, length--;
                while(line[start - 1] == character);
                // std::cout << "start: " << start << " length: " << length << std::endl;
            }
            length++;
            // std::cout << "length: " << length << std::endl;
        }
        if(maxLength < length) maxLength = length;
        // std::cout << "\nmaxlength: " << maxLength << std::endl;
    }
    std::cout << maxLength << std::endl;

    return 0;
}