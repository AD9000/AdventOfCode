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
    int c = 0;
    while (cin >> start)
    {
        cin >> dash >> end >> letter >> colon >> line;

        int count = 0;
        for (int i = 0; i < line.size(); i++)
        {
            // frequency
            if (line[i] == letter)
            {
                count++;
            }
        }

        if (count <= end && count >= start)
        {
            c++;
        }
    }
    cout << c << endl;

    return 0;
}
