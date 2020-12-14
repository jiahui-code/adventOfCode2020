import re

def is_passport(info_str):
    """has 8 column is valid passport"""
    columns = info_str.count(':')
    if columns == 8:
        return is_valid_info(info_str)
    elif columns == 7 and not ('cid:' in info_str):
        return is_valid_info(info_str)
    return False

def is_hair(str):
    '''meet haring requirement'''
    return (re.match(r"^#[A-Fa-f0-9]{6}$", str) and True)

def is_height(str):
    '''meet height requirement'''
    if str[-2:] == 'cm':
        return 150 <= int(str[:-2]) <= 190 and True
    elif str[-2:] == 'in':
        return 59 <= int(str[:-2]) <= 76 and True
    else:
        return False


def is_valid_info(info_str):
    info_str = info_str.replace('\n', ' ')
    info_list = info_str.split(' ')
    # seperate info by odd/even, even for key, odd for value
    info_dict = {x:y for (x, y) in (item.split(":") for item in info_list)}
    # print(info_dict)
    # byr and iyr limits
    return 1920 <= int(info_dict["byr"]) <= 2020 and 2010 <= int(info_dict["iyr"]) <= 2020 and \
        2020 <= int(info_dict["eyr"]) <= 2030 and \
            is_height(info_dict['hgt']) and \
            is_hair(info_dict['hcl']) and \
            info_dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
                info_dict['pid'].isdigit() and len(info_dict['pid']) == 9
            

test = {"60in", "190cm", "190in",'190'}
for i in test:
    print(is_height(i))


with open('adv4_input.txt') as input_handle:
    test_list = input_handle.read().split('\n\n')
    # short_test = test_list[:8]
    # print(short_test[-1])
    count = 0
    for passport in test_list:
        try:
            stat = is_passport(passport)
            # print(stat)
            count += 1 if stat else 0
        except:
            print(passport)
        # print(is_passport(passport))
    print(count)