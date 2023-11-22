words = input().upper()
words_list = list(set(words))

cnt_list = []
for i in words_list:
    cnt = words.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(words_list[max_index])
