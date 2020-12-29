def is_prea(pre_list, check_len) -> bool:
    #check last element of the list match preamble
    check = pre_list[-1]
    chk_lst = pre_list[-check_len-1 :-1]
    for list_num in chk_lst:
        rest = check - list_num
        if rest != list_num and rest in chk_lst:
            return True
    return False

with open('short.txt') as f_hand:
    in_list = list(map(int, f_hand.read().splitlines()))
    for i in range(25+1, len(in_list)+1):
        if not is_prea(in_list[:i], 25):
            # check list not include the last i element, so i-1 element is the one
            print(in_list[i-1])
            break
