import copy 

def switch(seat_list):
    '''return swtich seat list, must be padded before'''
    switched = copy.deepcopy(seat_list)
    width = len(seat_list[0])
    for ri in range(1, len(seat_list) - 1):
        for ci in range(1, width - 1):
            pos = seat_list[ri][ci] #seat check
            arnd_grid = seat_list[ri-1][ci-1:ci+2] + [seat_list[ri][ci-1]]\
                 + [seat_list[ri][ci+1]] + seat_list[ri+1][ci-1:ci+2] # seats around
            arnd_ocp = arnd_grid.count('#')
            if pos == 'L':
                switched[ri][ci] = '#' if arnd_ocp == 0 else 'L'
            elif pos == '#':
                switched[ri][ci] = 'L' if arnd_ocp >= 4 else '#'
            else:
                continue
    return switched


with open("short.txt") as file_h:
    # the seats are 2d list
    row_lst = file_h.read().splitlines()
    grid = [['0'] + list(line)+ ['0'] for line in row_lst]
    # add wrapper to avoid index error, ignore border case
    width = len(grid[0])
    grid.insert(0, ['0'] * width)
    grid.insert(len(grid), ['0'] * width)
    i, cnt_ocp = 0, 0
    while True: #switch unstil not changed 
        after = switch(grid)
        if after == grid:
            print(i)
            break
        else:
            grid, i = after, i+1
    for line in after:
        cnt_ocp += line.count('#')
