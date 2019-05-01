#include <iostream>
using namespace std;
int fun(int n)
{
    if (n>0)
    {
        if (1 == n)
        {
            return 1;
        }
        else if (2 == n)
        {
            return 2;
        }
        else
        {
            return fun(n-1) +fun(n-2);
        }
    }
    else
        return 0;
}

int main()
{
    int n;

    while(cin>>n)
        cout<<fun(n)<<endl;
    return 0;
}
