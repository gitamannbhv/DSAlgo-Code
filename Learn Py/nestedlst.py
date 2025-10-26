'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    slist=[]
    glist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        slist.append([name, score])
        glist.append(score)
    glist.sort()
    slist.sort()
    scnd_lowest=0
    for i in glist:
        if(i!=glist[0]):
            scnd_lowest=i
            break
    for i in range(0, len(slist)):
        if(slist[i][1]==scnd_lowest):
            print(slist[i][0])
