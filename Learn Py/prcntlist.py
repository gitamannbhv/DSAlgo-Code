'''wsl --unregister <DistributionName>'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks=student_marks[query_name]
    total=sum(query_marks)
    count=len(query_marks)
    avg=total/count
    print(f"{avg:.2f}")
    
