lines = []
for _ in range(5):
    line = input()
    lines.append(line)

result = ''
for i in range(max(len(line) for line in lines)):
    for j in range(5):
        if i < len(lines[j]):
            result += lines[j][i]

print(result)
