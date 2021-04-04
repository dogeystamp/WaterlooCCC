/* Written by DogeyStamp during the 2021 CCC.
 * 15/15 points
 * This uses the same time sum function as the brute force solution, and does binary search on it.
 * If you graph the total sum of time needed for each position, it makes an u shape.
 * Binary search finds the bottom of this u shape and prints it out.
 * hi is the maximum position that we think might be the answer.
 * lo is the minimum position that we think might be the answer.
 * The algorithm tightens the list of possible answers until there's only one left.
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

    long long lo = minp;
    long long hi = maxp;
    long long mid = -1;

    while(hi - lo > 1)
    {
        mid = lo + (hi-lo)/2;
        if(tsum(mid-1)<tsum(mid+1))
        {
            hi = mid;
        }
        else
        {
            lo = mid;
        }
    }

    cout << min(tsum(lo), tsum(hi));
}
