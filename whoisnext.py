#!/usr/bin/env python3

dictionary = {
    '0': 'Sheldon',
    '1': 'Leonard',
    '2': 'Penny',
    '3': 'Rajesh',
    '4': 'Howard'
}
def whoIsNext(names, r):
    # print(names)
    # print(r)
    queue = [0,1,2,3,4]
    result = 0
    for i in range(r):
        result = queue[0]
        queue = queue[1:]
        queue.append(result)
        queue.append(result)
    #print(result)
    print(queue)
    return dictionary[str(result)]

print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"],75))