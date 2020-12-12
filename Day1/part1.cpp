#include <iostream>
#include <climits>
#include <unordered_set>
using namespace std;

#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);

int main()
{
    FASTIO;

    unordered_set<int> s;
    int num;
    int sum = 2020;
    while (cin >> num)
    {
        if (s.find(sum - num) == s.end())
        {
            s.insert(num);
        }
        else
        {
            cout << (num * (sum - num)) << endl;
            break;
        }
    }

    return 0;
}
