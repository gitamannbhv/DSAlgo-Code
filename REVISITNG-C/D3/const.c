#include<stdio.h>
#define PI 3.14

int main(int argc, char const *argv[])
{
    /* code */
    const int a = 5;
    int b = 6;
    b = 4; //can be changed anywhere later in code and thus a variable.

    /* a = 10; */ //can't be changed and shows error and thus a constant, if detected compiler terminates the program there itself.

    printf("value of constant a int is = %d\n", a);
    printf("value of pi from preprocessor is = %.2f", PI);

    return 0;
}
