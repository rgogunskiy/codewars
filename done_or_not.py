#!/usr/bin/env python3

def does_list_have_dups(list):
    tmp = {}
    # print(list)
    # print('list_size', len(list))
    for i in list:
        tmp[i] = int(tmp.get(i,0)) + 1
    for _, value in tmp.items():
        if value > 1:
            return True
    return False

def region_to_row(region):
    tmp = []
    for i in range(len(region)):
        for j in range(len(region[i])):
            tmp.append(region[i][j])

    return tmp

def is_all_regions_done(board):
    region_size = 3
    for i in range(0, len(board), region_size):
        for j in range(0, len(board), region_size):
            tmp = []
            for z in range(region_size):
                tmp.append(board[i + z][j:j + region_size])
            if does_list_have_dups(region_to_row(tmp)):
                return False

    return True

def done_or_not(board): #board[i][j]
    # your solution here
    # ..
    # return 'Finished!'
    # ..
    # or return 'Try again!'
    finished = True
    is_done = 'Finished!'
    is_not_done = 'Try again!'
    for row in board:
        if does_list_have_dups(row):
            return is_not_done

    j = 0
    while j < len(board[0]):
        tmp = []
        i = 0
        while i < len(board):
            tmp.append(board[i][j])
            i += 1
        j += 1
        # print(tmp)
        if does_list_have_dups(tmp):
            return is_not_done

    if not is_all_regions_done(board):
        return is_not_done

    # if finished:
    #     return 'Finished'
    # else:
    #     return 'Try again!'
    return is_done

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
