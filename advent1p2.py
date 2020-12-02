with open('adv1_input.txt') as input_handle:
    cost_list = list(map(int, input_handle.read().splitlines()))
    big_list = [x for x in cost_list if x >= 1000]
    small_list = [x for x in cost_list if x < 1000]
    print(len(small_list))
    small_combines = []
    for number1 in small_list:
        combine = [number1, 0, 0]
        smaller = small_list[:]
        smaller.remove(number1)
        for number2 in smaller:
            combine[1] = number2
            smallest = smaller[:]
            smallest.remove(number2)
            for number3 in smallest:
                combine[2] = number3
                small_combines.append(combine)
    
    for combine in small_combines:
        if sum(combine) == 2020:
            print(combine)
            result = 1 
            for num in combine:
                result *= num
            print(result)
            break