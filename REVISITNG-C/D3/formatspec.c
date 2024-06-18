#include<stdio.h>

int main(int argc, char const *argv[])
{
    /* code */
    int a = 5;
    float b = 4.325;

    printf("no. a = %d and no. b = %f\n", a, b);
    printf("value of b upto 2 decimal places = %0.2f\n", b);

    printf("value of b with offset of 3 with 1 decimal points = .%6.1f.\n", b);
    //aforementioned line means; print the number with accuracy of 1 decimal point in 6 character spaces
    
    printf("value of b with offset of -3 with 1 decimal points = .%-6.1f.\n", b);
    //aforementioned line means; print the number with accuracy of 1 decimal point in 6 character spaces offset towards right

    return 0;
}
