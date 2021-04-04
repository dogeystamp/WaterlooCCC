/* Written by DogeyStamp during the 2021 CCC.
 * 3/15 points
 * I wrote this to get as much points as possible, even though I have no idea how to solve this fully.
 * This solution uses the fact that the first subtask is only even/odd and that it's easy to see if a section has the same GCD.
 */ 

//get partial points (3 marks) on S5

#include <bits/stdc++.h>
#include <cstring>

using namespace std;

bool even[2001];
bool ans[2001];

int main()
{
    int n, m;
    cin >> n >> m;
    vector<array<int,2>> qse;
    vector<array<int,2>> qso;

    memset(even,0,sizeof(even));
    memset(ans,0,sizeof(ans));

    for(int i = 0; i < m; i++)
    {
        int x,y,z;
        cin >> x >> y >> z;
        if(z == 1)
        {
            qso.push_back({x,y});
        }
        else
        {
            qse.push_back({x,y});
        }
    }

    for(auto q : qse)
    {
        for(int j = q[0]; j <= q[1]; j++)
        {
            even[j] = true;
            ans[j] = true;
        }
    }
    for(auto q : qso)
    {
        bool complete = false;
        for(int j = q[0]; j <= q[1]; j++)
        {
            if(!even[j])
            {
                complete = true;
                break;
            }
        }
        if(!complete)
        {
            cout << "Impossible";
            return 0;
        }
    }
    for(int i = 1; i <= n; i++)
    {
        if(!ans[i])
        {
            cout << "1";
            if(i != n) cout << " ";
        }
        else
        {
            cout << "2";
            if(i != n) cout << " ";
        }
    }
}
