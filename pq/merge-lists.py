#that accepts any number of lists and returns one merged list. 

input_lists = input("enter your lists here: ")
input_lists = "12 24 35 65 24 65 77,34 234 35 45 2 34 345 3,43 23 4 54 54 52 34 3"

lists = input_lists.split(",")
print(lists)

all_lists = []

for i in range(0, len(lists)):
    lst = lists[i].split()
    lst = list(map(int, lst))
    all_lists.append(lst)



def merge_lists(lists):
    result = []
    for i in lists: #for i in range(0, len(lists)) i = 0,1,2,3,4, .. for i in lists i = [12,24,1,24,53,5], [2,43,5,1,234,343]
        result.extend(i)
    return result


answer = merge_lists(all_lists)

print(answer)

"""
a = [1,2,3,4,5,6]

for i in range(0, len(a)) | for i in a
iter 1 :  0 | 1
iter 2 :  1 | 2

b = [[1,2,3], [4,5,4], ["a", "b"], [1,2,4,4,[3,4,[4,4,5]]]]

iter 1: 0 | [1,2,3] => i[2] = 3
iter 2: 1 | [4,5,4]
iter 3: 2 | ["a", "b"]
iter 4: 3 | [1,2,4,4,[3,4,[4,4,5]]] => i[2][1] =index out of range => i[4][2][2] = 5

"""



