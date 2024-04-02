// https://github.com/dogeystamp
// this code has changes made post-contest
// sorry for not documenting it much but this is contest code + bugfixes

#include <bits/stdc++.h>

using namespace std;

int n;
vector<array<int, 3>> a;
vector<array<int, 3>> b;
vector<array<int, 3>> moves;

int raidx(int i) {
	return a[i][2] + a[i][1] - 1;
}
int rbidx(int i) {
	return b[i][2] + b[i][1] - 1;
}
int laidx(int i) {
	return a[i][2];
}
int lbidx(int i) {
	return b[i][2];
}

void shifL(int i) {
	int need = laidx(i) - lbidx(i);
	if (need <= 0) return;
	if (laidx(i-1) >= lbidx(i)) {
		if (i != 0) {
			shifL(i-1);
		}
	}
	moves.push_back({false, laidx(i) - need, laidx(i)});
	if (i != 0) {
		int nrb = min(raidx(i-1), laidx(i) - need);
		a[i-1][1] = nrb - laidx(i-1);
	}
	a[i][2] -= need;
	a[i][1] += need;
}

void shifR(int i) {
	int need = rbidx(i) - raidx(i);
	if (need <= 0) return;
	if (raidx(i+1) <= rbidx(i)) {
		if (i != int(a.size())-1) {
			shifR(i+1);
		}
	}
	moves.push_back({true, raidx(i), min(raidx(i) + need, n-1)});
	if (i != int(a.size())-1) {
		int nrb = raidx(i+1);
		int nlb = max(laidx(i+1), raidx(i)+need);
		a[i+1][1] = nrb - nlb+1;
		a[i+1][2] = nlb;
	}
	a[i][1] += need;
}

void shif(int i) {
	if (lbidx(i) < laidx(i)) {
		shifL(i);
	} if (raidx(i) < rbidx(i)) {
		shifR(i);
	}
}

int main() {
	cin >> n;

	vector<int> raw_raw_a;
	vector<int> raw_raw_b;
	vector<array<int, 3>> raw_a;

	int last = -1;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		raw_raw_a.push_back(a);
		if (a == last) {
			raw_a[raw_a.size()-1][1]++;
		} else {
			last = a;
			raw_a.push_back({a, 1, i});
		}
	}
	last = -1;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		raw_raw_b.push_back(a);
		if (a == last) {
			b[b.size()-1][1]++;
		} else {
			last = a;
			b.push_back({a, 1, i});
		}
	}

	if(true) {
		cout << n << endl;
		for (int i = 0; i < n; i++) {
			cout << raw_raw_a[i] << " \n"[i == n-1];
		}
		for (int i = 0; i < n; i++) {
			cout << raw_raw_b[i] << " \n"[i == n-1];
		}
	}

	int aptr = 0;
	for (auto i = b.begin(); i != b.end() && aptr < raw_a.size(); i++) {
		while (aptr < raw_a.size() && raw_a[aptr][0] != (*i)[0]) {
			aptr++;
		}
		if (aptr < raw_a.size()) {
			a.push_back(raw_a[aptr]);
		} else {
			break;
		}
	}

	if (a.size() < b.size()) {
		cout << "NO\n";
		return 0;
	} else {
		cout << "YES\n";
	}

	for (int i = 0; i < int(a.size()); i++) {
		shif(i);
	}

	if (moves.size() > n) {
		assert(false);
		return 1;
	}

	cout << moves.size() << endl;
	for (auto mov : moves) {
		cout << (mov[0] ? "R" : "L") << " " << mov[1] << " " << mov[2] << "\n";
	}

	return 0;
}
