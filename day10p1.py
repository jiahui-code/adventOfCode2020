with open('short.txt') as file_h:
    in_lst = list(map(int, file_h.read().splitlines()))
    in_lst.append(0) # add starter 0 jolt
    in_lst.sort() # sort by sml to large
    print(in_lst)
    gap_lst = [in_lst[i+1] - in_lst[i] for i in range(len(in_lst) -1)]
    print(gap_lst)
    c_1 = gap_lst.count(1) # count gap of 1 numbers
    c_3 = len(gap_lst) - c_1 + 1 # alway add 3 of last one
    print(c_1, c_3, c_3 * c_1)
# part 2
