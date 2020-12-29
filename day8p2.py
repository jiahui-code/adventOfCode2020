import copy

def is_rep(d_dict):
    i, accumulator, dict_len = 0, 0, len(d_dict)
    while i <= dict_len and len(d_dict[i]) < 4: 
        # print('before', cmd_dict[i], 'len is', len(cmd_dict[i]))
        if d_dict[i][0] == 'nop':
            i += 1
        elif d_dict[i][0] == 'acc':
            accumulator += int(d_dict[i][1]) 
            i += 1
        else:
            i += int(d_dict[i][1])
        # if next index is equal to the length of dict, then dict is ran out
        if i >= dict_len:
            return accumulator
        d_dict[i].append(accumulator)
    return False

with open('day8_input.txt') as file_hand:
    cmd_list = file_hand.read().splitlines()
    # create a dictionary, order:[type, number, times]
    cmd_dict = {i:line.split() for (i,line) in list(enumerate(cmd_list))}
    for line in cmd_dict:
        cmd_type = cmd_dict[line][0]
        if cmd_type in ['jmp', 'nop']:
            # create a dict copy to change one line and check
            cmd_dict_cp = copy.deepcopy(cmd_dict)
            cmd_dict_cp[line][0] = 'nop' if cmd_type == 'jmp' else 'jmp'
            result = is_rep(cmd_dict_cp)
            if result:
                print(result)
                break