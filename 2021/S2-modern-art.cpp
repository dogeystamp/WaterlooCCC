/* Written by DogeyStamp during the 2021 CCC.
 * 15/15 points
 * If you wrote a naive solution where you keep track of each grid cell, it would be too slow.
 * Here, instead of setting each grid cell one at a time when the artist paints a stroke,
 * we set a bool value in an array.
 * ro[ind] = !ro[ind] means "set ro[ind] to its opposite".
 * At the end, the code iterates over each grid and if it's coloured, it increments the count.
 *
 * This solution is non optimal, however it does run fast enough to get all the points.
 */ 

#include <bits/stdc++.h>
#include <cstring>
#define sz 5000000

using namespace std;

bool ro[sz];
bool co[sz];

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    int m, n, k;
    cin >> m >> n >> k;

    memset(ro, 0, sizeof(ro));
    memset(co, 0, sizeof(co));

    for(int i = 0; i < k; i++)
    {
        string stroke;
        int ind;
        cin >> stroke >> ind;
        ind--;

        bool s = stroke == "R";
        if(s)
        {
            ro[ind] = !ro[ind];
        }
        else
        {
            co[ind] = !co[ind];
        }
    }

    int count = 0;

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if((ro[i]||co[j]) && !(ro[i]&&co[j]))
            {
                count++;
            }
        }
    }
    cout << count;
}
