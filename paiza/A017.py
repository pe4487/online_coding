# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
"""
H W N
h_1 w_1 x_1
h_2 w_2 x_2
...
h_N w_N x_N
"""

input_line = input()
h, w, n = input_line.split(' ')
mt = []
for i in range(int(h)):
    mt.append(['.' for j in range(int(w))])

for i in range(int(n)):
    rec = input()
    rec_h, rec_w, rec_x = rec.split(' ')
    is_safe = True
    for base_idx in reversed(range(int(h))):
        for row_index in reversed(range(int(rec_h))):
            row_index = base_idx - row_index
            if row_index < 0:
                break
            for col_index in range(int(rec_w)):
                col_index += int(rec_x)
                if mt[row_index][col_index] == '.':
                    #print(row_index, col_index, "ok")
                    pass
                elif mt[row_index][col_index] == '#':
                    #print(row_index, col_index, "no")
                    is_safe = False
        if is_safe: 
            continue
        else:
            break

    for row_index in reversed(range(int(rec_h))):
        if is_safe:
            row_index = base_idx + row_index
        else:
            row_index = base_idx - row_index + 1
        if row_index < 0:
            continue
        for col_index in range(int(rec_w)):
            col_index += int(rec_x)
            #print(row_index, col_index)
            mt[row_index][col_index] = '#'

    """
    for row in mt:
        s = ""
        for ele in range(len(row)):
            s += row[ele]
        print(s)
    print("=========round %s======" % i)
    """

mt.reverse()
for row in mt:
    s = ""
    for ele in range(len(row)):
        s += row[ele]
    print(s)
