with open('adv3_input.txt') as input_handle:
    grid = input_handle.read().splitlines()
    start, count = 0, 0
    
    # for line in grid:
    #     try:
    #         count += 1 if line[start] == '#' else 0
    #     except:
    #         print('end of line now.')
    #         break
    #     finally:
    #         start += 3
    print(count)