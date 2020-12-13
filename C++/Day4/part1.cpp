#include <iostream>
#include <vector>
#include <climits>
#include <cstring>
using namespace std;

#define N 1500
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

vector<string> split(string line, char delim)
{
    vector<string> spl;

    string word;
    for (int i = 0; i < line.size(); i++)
    {
        if (line[i] == delim || line[i] == '\n')
        {
            if (word.size() > 0)
            {
                spl.pb(word);
            }
            word.clear();
        }
        else
        {
            word += line[i];
        }
    }

    return spl;
}

int main()
{
    FASTIO;

    string line;
    while (getline(cin, line))
    {
        cout << line << " " << (line == "\n") << endl;
        if (line == "\n")
        {
            continue;
        }

        // char *cline = new char[line.size() + 1];
        // copy(line.begin(), line.end(), cline);
        // char *test = strtok(cline, " ");

        // delete[] cline;
        vector<string> t = split(line, ' ');

        for (auto w : t)
        {
            cout << w << endl;
        }
        cout << "------" << endl;
    }

    return 0;
}
