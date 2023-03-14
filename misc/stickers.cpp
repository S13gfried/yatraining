#include <vector>
#include <set>
#include <iostream>
#include <vector>

int main()
{
    int sticker_count;
    std::cin >> sticker_count;

    std::set<int> stickers;
    int buffer;
    for(int i = 0; i < sticker_count; i++)
    {  
        std::cin >> buffer;
        stickers.insert(buffer);
    }

    int size = stickers.size();

    std::vector<int> sticker_list(0);

    for(int sticker : stickers)
        sticker_list.push_back(sticker);

    int queries;
    std::cin >> queries;

    for(int i = 0; i < queries; i++)
    {
        int limit;
        std::cin >> limit;
        int low = 0, high = size - 1, total = size;
        
        while(low <= high)
        {
            //std::cout << "low: " << low << " high: " << high << std::endl;
            int mid = (low + high) / 2;
            if(sticker_list[mid] >= limit)
                {
                    total = mid;
                    high = mid - 1;
                } 
            else
                    low = mid + 1;
        }
        std::cout << total << std::endl;
    }

    return 0;
}