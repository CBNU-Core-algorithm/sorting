#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    //변수
    int team_L = 0;
    int team_O = 0;
    int team_V = 0;
    int team_E = 0; //팀 LOVE
    int human_L = 0;
    int human_O = 0;
    int human_V = 0;
    int human_E = 0; // 사람 LOVE
    string human_name;//사람 이름
    int team_name_number=0; //팀 개수
    int score=0; //최종 점수
    int standard=0; //최종 점수 비교값
    int index=0; //최종 점수 인덱스

    //입력
    cin >> human_name; 
    cin >> team_name_number;

    vector<string> team_name(team_name_number); //팀 이름
    string name; //팀이름 임시저장

    for (int h = 0; h < human_name.length(); h++) { //사람이름에서 LOVE개수 확인
        if (human_name.at(h) == 'L') {
            human_L++;
        }
        if (human_name.at(h) == 'O') {
            human_O++;
        }
        if (human_name.at(h) == 'V') {
            human_V++;
        }
        if (human_name.at(h) == 'E') {
            human_E++;
        }
    }

    for (int i = 0; i < team_name_number; i++) { //팀이름 입력
        cin >> name;
        team_name.push_back(name);
    }
    sort(team_name.begin(), team_name.end()); //정렬

    for (int i = 0; i < team_name_number; i++) {
        for (int j = 0; j < team_name[i].length(); j++) {
            if (team_name[i].at(j)=='L') {
                team_L++;
            }
            if (team_name[i].at(j) == 'O') {
                team_O++;
            }
            if (team_name[i].at(j) == 'V') {
                team_V++;
            }
            if (team_name[i].at(j) == 'E') {
                team_E++;
            }                
        }
        //토탈 러브 계산
        score = ((human_L + team_L + human_O + team_O) * (human_L + team_L + human_V + team_V) * 
            (human_L + team_L + human_E + team_E) * (human_O + team_O + human_V + team_V) * 
            (human_O + team_O + human_E + team_E) * (human_V + team_V + human_E + team_E)) % 100;
        if (score > standard) {
            standard = score;
            index = i;
        }
    }
    //가장 점수가 높은 이름 출력
    cout << team_name[index];
}
