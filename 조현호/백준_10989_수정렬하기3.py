import sys
# sys.stdin = open('a.txt', 'rt') # 테스트용 코드
input = sys.stdin.readline

# 계수정렬을 통해 값 입력받기 ( 데이터 범위가 작다면, O(N)에 가까운 성능을 낼 수 있다. )
cnt_list = [0] * 10001 # 1 ~ 10000 까지의 자연수 인덱스를 만드려면, 10001개의 리스트를 만들어야 한다.
n = int(input())
for i in range(n):
    cnt_list[int(input())] += 1

# 정답 출력
for i in range(1, len(cnt_list)):
    for _ in range(cnt_list[i]):
        print(i)
