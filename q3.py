"""
Question3
Create a function that takes a string and returns a string with its letters in alphabetical
order.
Examples
alphabet_soup("hello") ➞ "ehllo"
alphabet_soup("edabit") ➞ "abdeit"
alphabet_soup("hacker") ➞ "acehkr"
alphabet_soup("geek") ➞ "eegk"
alphabet_soup("javascript") ➞ "aacijprstv"
"""

def alphabet_soup(s):
    return ''.join(sorted(s))

s = input("Enter String ")
s1 = alphabet_soup(s)
print("alphabet_soup(",s,") ➞",s1)