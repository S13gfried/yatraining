#include <vector>
#include <iostream>

struct solution
{
    int complexity;
    std::vector<int> sequence;
};

void printSolution(solution sol)
{
    std::cout << sol.complexity << "\n";
    int length = sol.sequence.size();

    for(int i = 0; i < length; i++)
    {
        std::cout << sol.sequence[i];
        if(i != length - 1)
            std::cout << " ";
    }
    std::cout << std::endl;
}

int main()
{

    int argument;
    std::cin >> argument;

    std::vector<solution> solutions = std::vector<solution>(argument);

    solutions[0] = {0, std::vector<int>{1}};

    for(int i = 1; i < argument; i++)
    {
         solutions[i] = solutions[i - 1];
        
         if((i % 2 == 1) && (solutions[i/2].complexity < solutions[i].complexity))
             solutions[i] = solutions[i/2];

         if((i % 3 == 2) && (solutions[i/3].complexity < solutions[i].complexity))
             solutions[i] = solutions[i/3];

         solutions[i].complexity += 1;
         solutions[i].sequence.push_back(i + 1);
    }
        printSolution(solutions[argument - 1]);
         return 0;
}