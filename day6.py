def group_count(group_ans) -> int:
    ans_set = set() 
    for char in group_ans:
        if char != '\n':
            ans_set.add(char)
    # print(ans_set)
    return len(ans_set)


with open('day6_input.txt') as input_handle:
    test_list = input_handle.read()
    test_list = test_list.split('\n\n')
    # print(test_list)
    count = 0
    for group in test_list:
        count += group_count(group)
    print(count)
    
 

