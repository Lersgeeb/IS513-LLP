#ifndef ADD_H  
#define ADD_H
class Addition  

{
    public:
        float add(float x, float y);
};
#endif


#include "add.h"

float Addition::add (float x, float y);
{
    float off;
    off=x+y;
    return off;
}


#include <iostream>
#include "add.h"

int main()
{
    Addition add;
    std::cout << "The sum of 3 and 4 is"<< add.add(3.0,4.0) << '\n';
    return 0;
}
