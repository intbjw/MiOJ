#include<bits/stdc++.h>
using namespace std;
int main()
{
	string str;

	while(cin>>str)
    {
        int a[129]={0},b[129]={0};
        for(int i=0;i<str.size();i++)
        {
            a[str[i]]++;
        }
        cin>>str;
        for(int i=0;i<str.size();i++)
        {
            b[str[i]]++;
        }
        int flag=1;
        for(int i=0;i<129;i++)
        {
            if(a[i]>b[i])
            {
                flag=0;
                break;
            }
        }
        if(flag)
            cout<<"true"<<endl;
        else
            cout<<"false"<<endl;
    }

	return 0;
}
