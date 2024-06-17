#include<stdio.h>

int main(int argc, char const *argv[])
{
    /* code */
    float a,b;
    printf("enter no. a and b each after enter");
    scanf("\n %d \n %d", &a, &b);

    printf("The sum is: %f\n", a+b);
    printf("The diff. is: %f\n", a-b);
    printf("The product is: %f\n", a*b);
    printf("The dividend is: %f\n", a/b);
    
    // printf("The reminder is: %f\n", a%b);

    return 0;
}
