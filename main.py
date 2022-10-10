words = input("Enter the list: ").split()
are = ['a', 'r', 'e']
are_input_list = []
for i in range(len(words)):
    idxlst = [words[i].find(are[j]) for j in range (len(are))]
    if idxlst[0] >= 0 and idxlst[1] >= 0 and idxlst[2] >= 0:
        are_input_list.append(words[i])
for i in range(len(are_input_list)):
    print(are_input_list[i], end=' ')