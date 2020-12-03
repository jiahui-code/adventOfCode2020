with open('adv3_input.txt') as input_handle:
    grid = input_handle.read().splitlines()
    start, count = 3, 0
    for line in grid[1:]:
        try:
            spot = line[start]
        except:
            start -= len(line)
            spot = line[start]
        finally:
            # print(start)
            # print(spot)
            count += 1 if spot == '#' else 0
            start += 3
    print(count)