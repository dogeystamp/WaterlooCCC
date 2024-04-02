// https://github.com/dogeystamp
// code written during contest

#include <bits/stdc++.h>

using namespace std;

bool test() {
	string s;
	cin >> s;
	int counts[26]{};
	for (char c : s) {
		counts[c - 'a']++;
	}
	for (int i = 1; i < s.size(); i++) {
		bool l1 = counts[s[i]-'a'] <= 1;
		bool l2 = counts[s[i-1]-'a'] <= 1;
		if (l1 == l2) {
			return false;
		}
	}
	return true;
}

int main() {
	int t, n;
	cin >> t >> n;
	for (int tc = 0; tc < t; tc++) {
		cout << (test() ? "T" : "F") << "\n";
	}
}
