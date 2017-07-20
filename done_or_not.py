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
    # TODO: check columns and region
    
    if finished:
        return 'Finished'
    else:
        return 'Try again!'


print(done_or_not([[0,1,2],
                   [0,1,2],
                  [0,1,2]]))