yd = input()
num = int(input())
tm_list = sorted([input() for i in range(num)])

max_r = max_i = 0
for i in range(num):
    L = yd.count('L') + tm_list[i].count('L')
    O = yd.count('O') + tm_list[i].count('O')
    V = yd.count('V') + tm_list[i].count('V')
    E = yd.count('E') + tm_list[i].count('E')
    R = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if R > max_r:
        max_r = R
        max_i = i
print(tm_list[max_i])


