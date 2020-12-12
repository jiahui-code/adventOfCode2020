import re

def is_passport(info_str):
    """has 8 column is valid passport"""
    columns = info_str.count(':')
    if columns == 8:
        return True
    elif columns == 7 and not ('cid:' in info_str):
        return True
    return False

def is_info_valid(info_str):
    info_str = info_str.replace('\n', ' ')
    info_str = info_str.replace(':', ' ')
    info_list = info_str.split(' ')
    info_dict = {x:y for x in info_list[::2] for y in info_list[1::2]}
    # return 1920 <= int(info_dict["byr"]) <= 2020 and 2010 <= int(info_dict["iyr"]) <= 2020 and \
    #     2020 <= int(info_dict["eyr"]) <= 2030 and \
    #         re.match(r"#[A-Fa-f0-9]{6}$", info_dict['hcl']) and \
    #         info_dict.['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
    #             re.match(r"^[0-9]{9}")
            

test = {'#asdfjh', '8sdfk', '#01seds'}
for i in test:
    print(True and re.match(r"#[A-Fa-f0-9]{6}$", i))

# with open('adv4_input.txt') as input_handle:
#     test_list = input_handle.read().split('\n\n')
#     print('----------')
#     count = 0
#     for passport in test_list:
#         count += 1 if is_passport(passport) else 0
#     print(count)