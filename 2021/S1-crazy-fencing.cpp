/* Written by DogeyStamp during the 2021 CCC.
 * 15/15 points
 * This code takes all the heights and widths and adds up areas.
 * At the moment I forgot it was a trapezoid and calculated it as a triangle with a rectangle instead.
 * The formula for a trapezoid is (b+B)*h/2 where b is the small side, B is the parallel long side, and h is the distance between the parallel sides (height).
 *
 * Here, the triangle formula is h*w/2 where h is the height of the triangle and w is its width.
 * abs(hs[i]-hs[i+1]) is h here.
 *
 * For the rectangle, the formula is width * height. The min() is so that it's the height of the rectangle,
 * not the height of the rectangle plus the height of the rectangle that we use in the formula.
 *
 */

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<double> hs;

    for(int i = 0; i < n+1; i++)
    {
        double h;
        cin >> h;
        hs.push_back(h);
    }

    double area = 0;

    cout << fixed;

    for(int i = 0; i < n; i++)
    {
        double w;
        cin >> w;
        //rectangle
        area += w*min(hs[i],hs[i+1]);
        //triangle
        area += w*abs(hs[i]-hs[i+1])/2;
    }
    cout << area;
}
