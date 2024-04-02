// https://github.com/dogeystamp
// code written during contest

#include <bits/stdc++.h>

using namespace std;

vector<int> hats;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		hats.push_back(a);
	}
	int i = 0;
	int j = n/2;

	int ans = 0;
	
	for (; i < n; i++, j++) {
		if (hats[i] == hats[j%n]) {
			ans += 1;
		}
	}

	cout << ans << endl;
}
