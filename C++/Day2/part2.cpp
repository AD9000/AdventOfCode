#include <iostream>
#include <cstring>
using namespace std;

#define FASTIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(0);                       \
    cout.tie(0);

int main()
{
    FASTIO;

    int start, end;
    char dash, letter, colon;
    string line;
    int count = 0;
    while (cin >> start)
    {
        cin >> dash >> end >> letter >> colon >> line;
        start--;
        end--;

        // xor: either one or the other
        if ((line[start] == letter) ^ (line[end] == letter))
        {
            count++;
        }
    }
    cout << count << endl;

    return 0;
}
