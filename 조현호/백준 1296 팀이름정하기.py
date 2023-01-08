import sys
# sys.stdin = open('a.txt', 'rt') # test용 코드
input = sys.stdin.readline

# 값 입력받기 (key : 이름 / value : 확률)
name = input().strip()
n = int(input())
name_dict = {}
for i in range(n):
    temp_name = input().strip()
    L = temp_name.count('L') + name.count('L')
    O = temp_name.count('O') + name.count('O')
    V = temp_name.count('V') + name.count('V')
    E = temp_name.count('E') + name.count('E')
    name_dict[temp_name] = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

# 확률이 가장 큰 팀을 찾아 리스트에 저장
max_value = max(name_dict.values())
has_max_keys = []
for key in name_dict.keys():
    if name_dict[key] == max_value:
        has_max_keys.append(key)

# 확률이 가장 큰 팀 중에서 사전순서가 가장 높은 팀을 출력
print(sorted(has_max_keys)[0])

