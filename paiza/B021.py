# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

"""
・末尾が s, sh, ch, o, x のいずれかである英単語の末尾に es を付ける
・末尾が f, fe のいずれかである英単語の末尾の f, fe を除き、末尾に ves を付ける
・末尾の1文字が y で、末尾から2文字目が a, i, u, e, o のいずれでもない英単語の末尾の y を除き、末尾に ies を付ける
・上のいずれの条件にも当てはまらない英単語の末尾には s を付ける
"""

input_line = input()
for i in range(int(input_line)):
    word = input()
    if word[-1] in ['s', 'o', 'x'] or word[-2:] in ['sh', 'ch']:
        words = word + "es"
    elif word[-1] in ['f']:
        words = word[:-1] + "ves"
    elif word[-2:] in ['fe']:
        words = word[:-2] + "ves"
    elif word[-1] in ['y']:
        if word[-2] not in ['a', 'i', 'u', 'e', 'o']:
            words = word[:-1] + "ies"
        else:
            words = word + "s" 
    else:
        words = word + "s"
    print(words)


