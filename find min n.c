#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_square(long long x)//judge whether is a square of an integer
{
    long long root=(long long)sqrt(x);
    return(root * root == x);
}

bool is_cube(long long x)//judge whether is a cube of a integer
{
    long long root=(long long)round(pow(x,1.0/3.0));
    return(root * root * root == x);
}

int main()
{
    long long n = 1;
    while (true)
    {
        if (n%2==0 && n%3==0)
        {
            if(is_cube(n/3) && is_square(n/2))//6|n and is_cube and is_square
            {
                printf("最小的正整数n是lld\n",n);
                break;
            }
        }
        
        n=n+1;
        
    }
    return 0;
    
}
