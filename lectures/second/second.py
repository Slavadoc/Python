# with open('data.txt', 'w') as data:
#     data.write('line 1 \n')
#     data.write('line 2 \n')

# colors = ['red', 'green', 'blue']
# data = open('data.txt', 'a')
# data.writelines(colors)
# data.close()

# path = 'data.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

import function as concatenation

# a = int(input())
# # b = int(input())
# s = [str(s) for s in input().split()]

# print(function.mul(a,b))
# print(function.new_string(s,b))
# print(concatenation('q', 's', 'd', 'w'))
# # Кортежи
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
#t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment

list1 = [1,2,3,4]
list2 = list1
list1[1] = 123
list1.pop()

for e in list1:
    print(e)
print()
for e in list2:
    print(e)
