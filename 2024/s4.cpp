// https://github.com/dogeystamp
// this code was written post-contest

#include <bits/stdc++.h>

using namespace std;

const int maxN = 2e5;

vector<array<int, 2>> adj[maxN];
bool vis[maxN] {};
// GRB
int edg[maxN] {};

void dfs(int cur, int col) {
	int ccol = col == 1 ? 2 : 1;

	vis[cur] = true;
	for (auto dest : adj[cur]) {
		int nd = dest[0];
		if (!vis[nd]) {
			edg[dest[1]] = ccol;
			dfs(nd, ccol);
		}
	}
}

int main() {
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int u, v;
		cin >> u >> v;
		u--; v--;
		adj[u].push_back({v, i});
		adj[v].push_back({u, i});
	}

	for (int i = 0; i < n; i++) {
		if (!vis[i]) dfs(i, 1);
	}

	for (int i = 0; i < m; i++) {
		switch (edg[i]) {
			case 0:
				cout << "G";
				break;
			case 1:
				cout << "R";
				break;
			case 2:
				cout << "B";
				break;
		}
	}
	cout << endl;
}
