#include <stdio.h>
#include <math.h>

//homework question2

int main()
{
    double a = 2.0;// calculate the real value of sqrt 2
    double x_prev = 1.0;//initial x=1.0
    double x_now;
    double accuracy = 1e-10;

    while (1)
    {
        x_now = 0.5*(x_prev + a/x_prev);
        if(fabs(x_now - x_prev ) <= accuracy)
        {
            printf("迭代最后的结果是%.10lf\n",x_now);
            break;
        }


        x_prev = x_now;


    }

    printf("根号二的真实值是%.10lf\n",sqrt(a));
    return 0;


}


