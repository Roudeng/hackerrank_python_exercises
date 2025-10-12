from collections import defaultdict

# n和m是size大小
n, m = map(int, input().split())

# 建構字典，key是字串，value是位置
d = defaultdict(list) # 處理了key未被設定過為空的情況，給空list作為預設值
# 法二
# d = {}

# 讀入A組的n個字串
for i in range(n):
    word = input().strip()
    # 法二
    # if word not in d:
    #     d[word] = []
    # d[word].append(i+1)
    d[word].append(i+1) # 位置要求為1-indexed，從1開始

# 處理B組的查詢
for _ in range(m):# 執行m次，變數用不到故用'_'
    query = input().strip()
    if query in d:
        print(*d[query]) # * unpacking解包，把list中的元素「拆開當作多個引數」傳進函式。比如從[1, 2, 3]到1 2 3
    else:
        print('-1')


