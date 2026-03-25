#include <stdio.h>
#include <math.h>

//用于寻找p*2=8q*2+1 的最小的10组解
int main()
{
    long long q = 1;      // 枚举初始值
    int count = 0;        // 用于记录已经找到的解的数量


    while (count < 10) 
    {
        long long p2 = 8 * q * q + 1;
        long long p = (long long)sqrt(p2);
        if (p * p == p2)
        {
            count++;
            printf("第 %2d 对: p = %-10lld q = %-10lld\n", count, p, q);
        }
        
        q++; 
    }

    return 0;
}