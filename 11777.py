n = int(input())
for i in range(n):
    marks = list(map(int, input().split()))
    t1 = marks[0]
    t2 = marks[1]
    f = marks[2]
    a = marks[3]
    ct = list()
    for j in range(4,len(marks)):
        ct.append(marks[j])

    ct = sorted(ct)
    ct_marks = (ct[2]+ct[1])//2
    total = 0
    total = t1+t2+f+a+ct_marks
    if total >= 90:
        print(f"Case {i+1}: A")
    elif total < 90 and total >= 80:
        print(f"Case {i+1}: B")
    elif total < 80 and total >= 70:
        print(f"Case {i+1}: C")
    elif total < 70 and total >= 60:
        print(f"Case {i+1}: D")
    else:
        print(f"Case {i+1}: F")