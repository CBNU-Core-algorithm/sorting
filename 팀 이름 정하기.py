yeondu_name = input("연두의 이름은:" )
team_name_list = input("team name list는").split()
number_of_teams = len(team_name_list)

love = []
lv_nm_ls = []
result = {}

#연두 이름에서 L,O,V,E 갯수세기
for k in yeondu_name:
    if 'L' == k:
        love[0] += 1
    elif 'O' == k:
        love[1] += 1
    elif 'V' == k:
        love[2] += 1
    elif 'E' == k:
        love[3] += 1

#팀 이름 하나하나 돌리면서 love리스트 횟수 추가하기
for i in team_name_list:
    team_name = list(i)
    for j in team_name:
        if 'L' == j:
            love[0] += 1
        elif 'O' == j:
            love[1] += 1
        elif 'V' == j:
            love[2] += 1
        elif 'E' == j:
            love[3] += 1
            lv_nm_ls[j] = love

#이환이 공식
for h in team_name_list :
    result = {h : (((lv_nm_ls[h][0]+lv_nm_ls[h][1])*(lv_nm_ls[h][0]+lv_nm_ls[h][2])*(lv_nm_ls[h][0]+lv_nm_ls[h][3])*(lv_nm_ls[h][1]+lv_nm_ls[h][2])*(lv_nm_ls[h][1]+lv_nm_ls[h][3])*(lv_nm_ls[h][2]+lv_nm_ls[h][3])) % 100)}

#우승할 확률이 가장 높은 팀 이름 출력
print(max(result, key = result.get))
