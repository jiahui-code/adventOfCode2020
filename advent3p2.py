def slop(grid, right, down):
    start, count = right, 0
    for line in grid[down::down]:
        try:
            spot = line[start]
        except:
            start -= len(line)
            spot = line[start]
        finally:
            # print(start)
            # print(spot)
            count += 1 if spot == '#' else 0
            start += right 
    return count

with open('adv3_input.txt') as input_handle:
    grid = input_handle.read().splitlines()
    slops = [(grid, *x) for x in [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]]
    times, result = [], 1
    for step in slops:
        trees = slop(*step)
        result *= trees
        times.append(trees)
    print(times, result)