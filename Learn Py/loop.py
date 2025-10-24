'''Task
The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.'''

if __name__ == '__main__':
    n = int(input())
    a = 0
    if 1<= n <=20:
        while a<n:
            print(a**2)
            a += 1
    else:
        print("enter val btw 1 to 20")
