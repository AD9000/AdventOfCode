#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>
using namespace std;

#define N 150010
#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);
#define INF INT_MAX
#define pb push_back
#define x first
#define y second
typedef long long ll;
typedef pair<ll, ll> pii;

int main()
{
    FASTIO;

    string line;
    cin >> line;

    // 3 right, 1 down, repeating pattern
    int columns = line.size();
    int col = 3;
    int count = 0;

    while (cin >> line)
    {
        if (line[col] == '#')
        {
            count++;
        }

        col = (col + 3) % columns;
    }

    cout << count << endl;

    return 0;
}
