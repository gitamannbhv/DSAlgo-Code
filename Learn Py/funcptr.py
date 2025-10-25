'''The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .'''

if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150:
        for i in range (1, n+1, 1):
            print(i, end="")
    else:
        print("enter value btw 1 to 150")
