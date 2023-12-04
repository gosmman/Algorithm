students = [i for i in range(1,31)]

for _ in range(28):
    A = int(input())
    students.remove(A)
    
print(min(students))
print(max(students))

