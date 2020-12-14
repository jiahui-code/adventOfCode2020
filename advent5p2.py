def bi_convert(info_str, char_for_1, char_for_0) -> str:
    """convert str to binary int"""
    info_str = info_str.replace(char_for_1, '1')
    info_str = info_str.replace(char_for_0, '0')
    return info_str

with open('adv5_input.txt') as input_handle:
    test_list = input_handle.read().splitlines()
    bi_list = [int(bi_convert(bi_convert(space, 'B', 'F'), 'R', 'L'), 2)
         for space in test_list]
    bi_list.sort()
    print(bi_list[0], bi_list[-1])
    for (front, back) in zip(bi_list[:-1], bi_list[1:]):
        if (back - front) == 2:
            print(back, front)
            result = back + 1
    

# print(bi_convert('BFBBBBBLLR', 'B', 'F'))
# print(bi_convert('BFBBBBBLLR', 'R', 'L'))
