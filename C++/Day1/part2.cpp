#include <iostream>
#include <vector>
#include <climits>
#include <unordered_set>
using namespace std;

#define N 1500
#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);

int nums[N];
int n;

int sum3(int a, int sum, int in)
{
    unordered_set<int> s;

    int total = sum - a;
    for (int i = 0; i < n; i++)
    {
        if (i == in)
        {
            continue;
        }

        if (s.find(total - nums[i]) == s.end())
        {
            s.insert(nums[i]);
        }
        else
        {
            return nums[i] * (total - nums[i]) * a;
        }
    }
    return 0;
}

int main()
{
    FASTIO;

    int i = 0;
    int num;
    while (cin >> num)
    {
        nums[i] = num;
        i++;
    }
    n = i;

    // part 2: 3 sum
    for (int j = 0; j < n; j++)
    {
        int x = sum3(nums[j], 2020, j);
        if (x > 0)
        {
            cout << x << endl;
            break;
        }
    }

    return 0;
}
