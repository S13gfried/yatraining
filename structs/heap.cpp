#include <iostream>
#include <vector>
#include <exception>

template<typename type>
std::vector<type> inputVector(int length)
{
    if(length < 0) throw std::invalid_argument("inputVector(), line __LINE__: invalid argument");

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

template<typename type, typename metrictype = type>
class Heap
{
    protected:
    std::vector<type> body;
    metrictype (*metric)(type arg);

    int getParent(int index) {return (index - 1) / 2; }
    int getChild(int index) {return index * 2 + 1; } //second child has index getChild() + 1


    int siftUp(int index)
    {
        while((index != 0) && (metric(body[getParent(index)]) < metric(body[index])))
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
                if(metric(body[getChild(index)]) > metric(body[index]))
                    swap(body[getChild(index)], body[index]);
                break;
            }

            type& child1 = &body[getChild(index)];
            type& child2 = &body[getChild(index) + 1];

            if((metric(child1) > metric(body[index])) && (metric(child1) >= metric(child2)))
            {
                swap(body[index], child1);
                index = getChild(index);
            }  
            else if ((metric(child2) > metric(body[index])) && (metric(child1) <= metric(child2)))
            {
                swap(body[index], child2);
                index = getChild(index) + 1;
            }
            else
                break;
        }
    }

    public:

    static min(type x) {return -(metrictype)x}
    static max(type x) {return (metrictype)x}

    template<typename iterable>
    Heap(iterable source = NULL, int size = 0, metrictype nmetric(type arg) = MAX)
    {
        body = std::vector<type>(0);
        metric = &nmetric;

        for(int index = 0; index < size; index++)
            push((source[index]);
    }

    void push(type item)
    {
        int index = body.size();
        body.push_back(item);
        siftUp(index);
    }   

    type pop()
    {
        type res = body[0];

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

    Heap<int> heap = Heap<int>(array, length);

    for(int index = 0; index < length; index++)
        std::cout << heap.pop();

    return 0;
}