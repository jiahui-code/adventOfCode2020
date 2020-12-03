def pw_is_valid(passwordline):
    limit_str, letter, password = passwordline.split(' ')
    least, most = list(map(int, limit_str.split('-')))
    # print(limit_str, letter, password, least, most)
    # print(password.count(letter[0]))
    check_front, check_back= password[least-1], password[most-1]
    if check_front != check_back and (check_back == letter[0] or \
        check_front == letter[0]):
        # print(password, letter[0], check_back, check_front)
        return True
    return False

with open('adv2_input.txt') as file_handle:
    all_pw = file_handle.read().splitlines()
    # print(all_pw[:5])
    count = 0
    for line in all_pw:
        # print(pw_is_valid(line))
        count += 1 if pw_is_valid(line) else 0
        # if pw_is_valid(line):
    print(count)