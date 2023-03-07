#include <iostream>
#include <vector>

template<typename type>
std::vector<type> inputVector(int length)
{
    std::vector<type> res = std::vector<type>(length);

    type buffer;
    for(int index = 0; index < length; index++)
    {
        std::cin >> buffer;
        res[index] = buffer;
    }

    return res;
}

template<typename type>
void swap(type& first, type& second)
{
    type buffer = first;
    first = second;
    second = buffer;
}

class Heap
{
    protected:
    std::vector<int> body;

    int getParent(int index) {return (index - 1) / 2; }
    int getChild(int index) {return index * 2 + 1; } //second child has index getChild() + 1


    int siftUp(int index)
    {
        while((index != 0) && (body[getParent(index)] > body[index]))
        {
            swap(body[getParent(index)], body[index]);
            index = getParent(index);
        } 
        return index;
    }


    int siftDown(int index)
    {
        while(getChild(index) < body.size())
        {
            if(getChild(index) + 1 == body.size()) //pre-terminal node has only one child
            {
                if(body[getChild(index)] < body[index])
                    swap(body[getChild(index)], body[index]);
                break;
            }

            int& child1 = body[getChild(index)];
            int& child2 = body[getChild(index) + 1];

            if((child1 < body[index]) && (child1 <= child2))
            {
                swap(body[index], child1);
                index = getChild(index);
            }  
            else if ((child2 < body[index]) && (child1 >= child2))
            {
                swap(body[index], child2);
                index = getChild(index) + 1;
            }
            else
                break;
        }
        return index;
    }

    public:

    Heap(std::vector<int> source)
    {
        body = std::vector<int>();

        for(int item : source)
            push(item);
    }

    void push(int item)
    {
        int index = body.size();
        body.push_back(item);
        siftUp(index);
    }   

    int pop()
    {
        int res = body[0];

        body[0] = body.back();
        body.pop_back();

        siftDown(0);
        return res;
    }
};

int main()
{
    int length;
    std::cin >> length;

    std::vector<int> array = inputVector<int>(length);

    Heap heap = Heap(array);

    for(int index = 0; index < length; index++)
    {
        std::cout << heap.pop();
        if(index != length - 1)
            std::cout << " ";
    }
    std::cout << std::endl;
    return 0;
}