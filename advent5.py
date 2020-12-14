def bigger_f(info_str, current_f, check_char):
    """find the seat with max f"""
    for i in range(len(info_str)):
        if info_str[i] != current_f[i]:
            return info_str if info_str[i] == check_char else current_f
        i += 1
    return info_str

def convert(string, check_char, max_num):
    '''conver string to int binary, 1 represent by check_char'''
    low, high = 0, max_num
    while len(string) >= 1:
        if string[0] == check_char:
            low = (high - low) // 2 + 1 + low
        else:
            high = (high - low) // 2 + low
        # print("low is {} high is {}".format(low, high))
        string = string[1:]
    return low


with open('adv5_input.txt') as input_handle:
    test_list = input_handle.read().splitlines()
    current_max = test_list[0][:-3]
    current_f = 0
    same_fb = []
    # find all lines with same FB part and put in same_fb list
    for line in test_list:
        fb_part = line[:-3]
        bigger = bigger_f(fb_part, current_max, 'B')
        if bigger == fb_part:
            if bigger == current_max:
                same_fb.append(line)
            else:
                same_fb = [line]
        current_max = bigger
    print(same_fb)
    seat_max = same_fb[0][-3:]
    for seat in same_fb:
        seat_max = bigger_f(seat[-3:], seat_max, 'R')
        if seat[-3:] == seat_max:
            seat_num = seat
    # seat_num = 'FBFBBFFRLR'
    print(seat_num)
    print(seat_num[:-3], seat_num[-3:])
    fb = convert(seat_num[:-3], 'B', 127)
    lr = convert(seat_num[-3:], 'R', 7)
    print(fb, lr)
    print(fb*8 + lr)

convert("FFFFFFF", "B", 127)

