from collections import Counter


s = input().strip() # .strip()在於去除開頭和結尾的空白和換行符等
if len(set(s)) < 3: # 三種不同的字元
    print('s-string has less than 3 distinct characters.')
else:
    a = Counter(s) # Counter({'q': 3, 'w': 2, 'z': 2, 'a': 1})
    a = list(a.items())
    # print(a) # [('w', 2), ('q', 3), ('a', 1), ('z', 2)] tuple清單
    a.sort(key=lambda x: x[0]) # 字母排序
    a.sort(key=lambda x: x[1], reverse=True) # 次數排序，x[1]取tuple的第二個值，預設升冪故加reverse
    for m, n in a[:3]:
        print(f'{m} {n}')
