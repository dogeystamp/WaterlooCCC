/* Written by DogeyStamp during the 2021 CCC.
 * 4/15 points
 * This is a brute force (naive) solution to the problem.
 * Here, I just iterate over each possible position and see the total time needed.
 */

#include <bits/stdc++.h>

using namespace std;

vector<array<long long,3>> friends;

long long tsum(long long ind)
{
    long long currsum = 0;
    for(auto fr : friends)
    {
        long long hear;
        if(ind > fr[0])
        {
            hear = max(ind-fr[2],fr[0]);
        }
        else
        {
            hear = min(ind+fr[2],fr[0]);
        }
        currsum += abs(hear-fr[0])*fr[1];
    }
    return currsum;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);

    int n;
    cin >> n;

    long long maxp = 0;
    long long minp = 1000000000;

    for(int i = 0; i < n; i++)
    {
        long long p,w,d;
        cin >> p >> w >> d;

        maxp = max(maxp, p);
        minp = min(minp, p);

        friends.push_back({p,w,d});
    }

    long long ans = 0xfffffffffffffff;

    for(int i = 0; i <= maxp; i++)
    {
        ans = min(ans, tsum(i));
    }
    cout << ans;
}
