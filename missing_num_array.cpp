#include <iostream>
using namespace std;

int main() {
    int test;
    cin  >> test;
    int number,temp;
    int out[test];
    for(int i=0;i<test;i++)
    {
        int n;
        cin >> n;
        number = (n*(n+1))/2;


        for(int j=0;j<n-1;j++)
        {
            cin >> temp;
            number = number - temp;

        }
        out[i] = number;

    }

    for( int i=0;i<test;i++)
        cout << out[i] << endl;

	return 0;
}
