import sys
# sys.stdin = open('a.txt', 'rt') # 테스트용 코드
input = sys.stdin.readline

# 값 입력받기
n = int(input())
time_list = []
for i in range(n):
    time_list.append(list(map(int, input().strip().split())))

# 일찍 끝나는 기준으로 오름차 정렬하는데, 끝나는 시간이 같은 경우는 시작시간 기준으로 오름차정렬
time_list.sort(key = lambda x : x[0])
time_list.sort(key = lambda x : x[1])

# 정렬된 리스트를 기준으로, 그리디알고리즘
cnt = 0
end = 0
for time in time_list:
    if time[0] >= end:
        cnt += 1
        end = time[1]

print(cnt)