big_match_dict = {}
small_march_dict = {}

def find(value, given_dict):
    '''find value in dict, return false if not found'''
    for key in given_dict:
        if given_dict[key] == value:
            print(key,"+", value, key+value)
            print("{} * {} = {}".format(key, value, key*value))
            return True
    return False

def update_dict(value, big):
    if big:
        big_match_dict[value] = big_match_dict.get(value, 2020 - value)
    else:
        small_march_dict[value] = small_march_dict.get(value, 2020 - value)
    return

with open('adv1_input.txt') as input_handle:
    cost_list = list(map(int, input_handle.read().splitlines()))
    for cost in cost_list:
        big = cost > 1020
        found = find(cost, small_march_dict if big else big_match_dict)
        if found:
            break
        else:
            update_dict(cost, big)
