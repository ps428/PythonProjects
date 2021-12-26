#include<iostream>
using namespace std;

int main(void)
{
    int i=0;
    for(i=0;i<=10;i++)
    {
        for(int j=0; j<=i; j++)
        {
            cout<<'-';
        }
        cout<<endl;
    } 

    return 0;
}