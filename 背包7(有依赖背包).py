"""树形dp转分组背包问题，每个节点都会有一个f[j],转换为分组背包从叶子节点向上运算
dp[u,i,j] 代表选了以u为根的子树, 只考虑其前i个子树时, 背包容量为j时, 可获得的最大价值 -> f[u][j]"""

import sys
import math

########################处理输入##############################
x = sys.stdin.readlines()
n, m = map(int, x.pop(0).rstrip().split())  # 物品数量、背包体积

y = [[] for i in range(len(x))]
for i in range(len(x)):
    y[i] = [int(j) for j in x[i].rstrip().split()]

f = [[0 for j in range(m + 1)] for i in range(n + 1)]
#########################代码主体##############################
h = [-1 for _ in range(n + 1)]
e = [0 for _ in range(n + 1)]
ne = [0 for _ in range(n + 1)]
v = [0 for _ in range(n + 1)]
w = [0 for _ in range(n + 1)]
idx = 1  # 边的序号


def addedge(a, b):  # 建立链式前向星，a起点指向b终点
    if a >= 0 and b >= 0:  # 起点、终点序号都得合法; 防止-1这种列表序号
        global idx
        e[idx] = b  # 终点
        ne[idx] = h[a]  # 同起点下一条边，构成链表效果
        h[a] = idx  # h的长度代表不同起点的数量, "当前边"就是以点a为起点的最后一条边
        idx += 1


def dfs(u):  # u代表子树的根节点，利用链式前向星进行dfs，起点代表树的父节点而终点代表子节点，叶节点指向-1
    global f
    i = h[u]  # 边的序号
    while i != -1:
        son = e[i]  # 子节点
        dfs(son)
        for j in range(m - v[u], -1, -1):  # 体积从大到小, 必拿本节点
            for k in range(1, j + 1):  # 分组背包问题，因为同个子树容量不同时，决策不同，决策之间互斥可以看作不同的物品
                f[u][j] = max(f[u][j], f[u][j - k] + f[son][k])  # 从子树更新最大价值情况
        i = ne[i]
    for i in range(m, v[u] - 1, -1):  # 背包容量足够就加上当前节点
        f[u][i] = f[u][i - v[u]] + w[u]
    for i in range(0, v[u]):  # 背包容量不够就不加当前节点，但是也不能放任何子节点
        f[u][i] = 0


def solution(n, m, items):
    # dp[u,i,j] 代表选了以u为根的子树, 只考虑其前i个子树时, 背包容量为j时, 可获得的最大价值 -> f[u][j]
    # 每算某个节点，先算它的子节点

    root = 0
    for i in range(1, len(items) + 1):  # i代表节点序号
        v[i], w[i], p = items[i - 1]
        if p == -1:
            root = i
        else:
            addedge(p, i)  # else可加可不加
    dfs(root)
    return f[root][m]


######################################################################################
print(solution(n, m, y))
