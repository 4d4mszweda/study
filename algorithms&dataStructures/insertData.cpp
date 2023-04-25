#include<iostream>
#include<stdlib.h>
#include<vector>
#include<sstream>

using namespace std;

int main()
{
    vector <string> tab;
    string word;
    while(cin>>word)
    {
        tab.push_back(word);
    }
    for( int i = 0; i < tab.size(); i++ )
    {
        if(tab[i]=="push")
        {
            int x;
            istringstream iss(tab[i+1]);
            iss>> x;
            cout << tab[i] << " " <<x<<endl;
            i++;
            continue;
        }
        cout << tab[ i ] << endl;
    }
}