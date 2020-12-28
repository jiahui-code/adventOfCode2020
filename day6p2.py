def all_yes_anwer(group_ans) -> int:
    ans_dict = {'\n':0}
    for char in group_ans:
        ans_dict[char] = ans_dict.get(char, 0) + 1
    # print(ans_set)
    line = ans_dict['\n'] + 1
    count = 0
    for yes_count in ans_dict.values():
        if yes_count == line:
            count += 1
    return count
    

with open('short.txt') as input_handle:
    test_list = input_handle.read()
    test_list = test_list.split('\n\n')
    # print(test_list)
    count = 0
    for group in test_list:
        count += all_yes_anwer(group)
    print(count)
    
 

