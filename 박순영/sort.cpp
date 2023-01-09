#include<iostream>
#include<vector>
using namespace std;

void insertion_sort(vector<int>& v, int totalnumber) {
	int swap; // 스왑할 떄 필요한 저장공간
	int i; //자리표시
	for (int j = 1; j < totalnumber; j++) { //저장공간 1부터 왼쪽과 비교하며 ,
		i = j;                              //작동할 때마다 저장공간을 1씩 증가시켜서 비교함
		while (true) {
			if (i == 0) { // 가장 좌측 저장공간을 만나면 while문을 빠져나감
				break;
			}
			else if (v[i-1] > v[i]) { // 가장 좌측에서 2번째부터 시작해서 좌측과 비교함. 좌측이 크다면
				swap = v[i]; //스왑 진행
				v[i] = v[i - 1];
				v[i - 1] = swap;
				i--; //다음 인덱스로 이동
			}
			else if (v[i] > v[i - 1]) { // 오름차순이 제대로 되어있다면 while문을 빠져나감
				break;
			}
		}
	}
	}

void input_number(vector<int>& v, int totalnumber) { //숫자 입력
	for (int i = 0; i < totalnumber; i++) {
		int number;	 //입력받는 각 숫자
		cin >> number;
		v.push_back(number); //저장공간에 넣음
	}
}

void result_print(vector<int>& v, int totalnumber) {//숫자 출력
	for (int i = 0; i < totalnumber; i++) {
		cout << v[i];
		cout << '\n';
	}
}

int main() {
	int totalnumber; //총 숫자 수
	cin >> totalnumber;
	vector<int> v; //동적저장공간
	input_number(v, totalnumber); //숫자 입력
	insertion_sort(v, totalnumber); // insertion sort 오름차순 설정 함수 실행
	result_print(v, totalnumber); //숫자 출력
}
