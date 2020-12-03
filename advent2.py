def pw_is_valid(passwordline):
    limit_str, letter, password = passwordline.split(' ')
    least, most = list(map(int, limit_str.split('-')))
    print(limit_str, letter, password, least, most)
    return

with open('adv2_input.txt') as file_handle:
    all_pw = file_handle.read().splitlines()
    print(all_pw[:5])
    pw_is_valid(all_pw[0])