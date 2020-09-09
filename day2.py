import copy
l = [1, 2, 3, 'a']
print('l=',l, len(l))
newVal = 10
l.append(newVal)
newList = [20, 30, 20]
l.extend(newList)
print('l=',l)
l.insert(0, 999)
print('l=',l)
tem = l.index(20, 7)
print(tem)
l2 = [i for i in l if not(isinstance(i, str))]
print('l2=',l2)
l2.sort(reverse=True)
print('l2=',l2)
# lst=copy.copy(l)
# lst.sort()
# print(lst)
# slicing list from start position till end or end position
print(l[2:6])
# reverese a list using reverse function
revLst = copy.copy(l)
revLst.reverse()
print('reverse of l=',revLst)
sorte = sorted(l2)
print('sorted l2=',sorte)
print('l2=',l2)
