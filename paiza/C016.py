# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
"""
A	4
E	3
G	6
I	1
O	0
S	5
Z	2
"""
d = {"A": "4", "E": "3","G": "6","I": "1","O": "0","S": "5","Z": "2"}
input_line = input()
ans = ""
for i in input_line:
    if d.get(i):
        ans += d.get(i)
    else:
        ans += i
print(ans)
