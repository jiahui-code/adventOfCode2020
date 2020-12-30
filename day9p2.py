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
    FOUND, NUM = i-1, in_list[i-1] # answer from Q1
    rvs_lst = in_list[FOUND-1::-1] # reverse list from start to Q1 answer number
    for i in range(len(rvs_lst)):
        tot, j = rvs_lst[i], i
        while tot < NUM:  # add one previous number if not exceed tartget
            j += 1
            tot += rvs_lst[j]
        if tot == NUM:
            rslt_lst = rvs_lst[i:j+1]
            print(sum(rslt_lst), max(rslt_lst), min(rslt_lst), max(rslt_lst)+min(rslt_lst))
            break
            