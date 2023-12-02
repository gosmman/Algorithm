my_list = []
a = list(map(int, input().split()))
my_list.append(a)
chess_list = [1, 1, 2, 2, 2, 8]
total_list = []

for i in range(len(a)):
    total_list.append(chess_list[i] - my_list[0][i])

for value in total_list:
    print(value, end=" ")