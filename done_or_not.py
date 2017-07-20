#!/usr/bin/env python3

def does_list_have_dups(list):
    tmp = {}
    print(list)
    for i in list:
        tmp[i] = int(tmp.get(i,0)) + 1

    # for _,v in tmp:
    #     if v > 1:
    #         return True
    for _, value in tmp.items():
        if value > 1:
            return True
    return False

def done_or_not(board): #board[i][j]
    # your solution here
    # ..
    # return 'Finished!'
    # ..
    # or return 'Try again!'
    finished = True

    for row in board:
        if does_list_have_dups(row):
            finished = False
    # TODO: check region
    j = 0
    while j < len(board[0]):
        tmp = []
        i = 0
        while i < len(board):
            tmp.append(board[i][j])
            i += 1
        j += 1
        print(tmp)
        if does_list_have_dups(tmp):
            finished = False

    
    if finished:
        return 'Finished'
    else:
        return 'Try again!'


print(done_or_not([[0,1,2],
                   [0,1,2],
                  [0,1,2]]))