#include <stdio.h>

int GCD(int x,int y)
{
   int i;
   for(i=x<y?x:y;i>0;i--)
   {
    if (x%i==0&&y%i==0)
    {
        //printf("The greatest common divisor is:%d",i);
        //use the upper line if needed
        break;
    }
   }
   return i;
}

int main()//This is least common multiple
{
    int x,y;
    printf("Please input two integers and split them with a space:");
    scanf("%d %d",&x,&y);
    printf("The least common multiple is:%d",x*y/GCD(x,y));
    return 0;
}