"""
Question1
Write a function that takes a list and a number as arguments. Add the number to the end of the
list, then remove the first element of the list. The function should then return the updated
list.
Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
next_in_line([], 6) ➞ "No list has been selected"
"""

def next_in_line(l,n):
    l = str_list(l)
    if len(l) == 0:
        return "No list has been selected"
    l.append(int(n))
    l.remove(l[0])
    return l

def str_list(l):
    l = l.split(' ')
    l1 = []
    for i in l:
        l1.append(int(i))
    return l1

l = input("Enter list in following form\n1 2 3 4\n:")
n = input("Enter no to be added ")
l1 = next_in_line(l,n)
print("next_in_line(",l,") ➞",l1)