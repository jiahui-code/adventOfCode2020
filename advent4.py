import re

def is_passport(info_str):
    """has 8 column is valid passport"""
    columns = info_str.count(':')
    if columns == 8:
        return True
    elif columns == 7 and not ('cid:' in info_str):
        return True
    return False


test = {'#asdfjh', '8sdfk', '#01seds'}
for i in test:
    print(True and re.match(r"#[A-Fa-f0-9]{6}$", i))

with open('adv4_input.txt') as input_handle:
    test_list = input_handle.read().split('\n\n')
    print('----------')
    count = 0
    for passport in test_list:
        count += 1 if is_passport(passport) else 0
    print(count)