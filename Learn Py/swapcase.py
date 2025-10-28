'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.'''

def swap_case(s):
    org_s=list(s)
    for i, char in enumerate(org_s):
        if char.islower():
            org_s[i] = char.upper()
        else:
            org_s[i] = char.lower()
    s="".join(org_s)
    return(s)

if __name__ == '__main__':
    s = input("enter you case")
    result = swap_case(s)
    print(result)