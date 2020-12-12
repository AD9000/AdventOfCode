#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>
using namespace std;

#define N 1500
#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
#define x first
#define y second
typedef long long ll;
typedef pair<int, int> pii;

int rows, columns;
string grid[N];

int findSlope(int right, int down)
{
    int col = right;
    int count = 0;

    for (int i = down; i < rows; i += down)
    {
        if (grid[i][col] == '#')
        {
            count++;
        }

        col = (col + right) % columns;
    }

    return count;
}

int main()
{
    FASTIO;

    rows = 0;
    while (cin >> grid[rows])
    {
        rows++;
    }

    columns = grid[0].size();

    ll ans = 1;
    vector<pii> moves = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}};
    for (auto move : moves)
    {
        cout << move.x << " " << move.y << " " << findSlope(move.x, move.y) << endl;
        ans *= findSlope(move.x, move.y);
    }

    cout << ans << endl;

    return 0;
}
