if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l1 = student_marks[query_name]
    result = sum(l1)/len(l1)
    print('%.2f' % result)
