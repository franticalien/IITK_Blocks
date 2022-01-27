#include <bits/stdc++.h>
#include "sha256.h"
 
using namespace std;
#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define fore(i, l, r) for (int i = int(l); i < int(r); ++i)
#define IFO std::ios::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL)
#define sum(c,l,r) pref[c][r+1]-pref[c][l]
typedef unsigned long long li;

const int INF = 1e9;

int a[100];

bool hex_greater(std::string &first, std::string &second)
{
    /* Comprasions based on size */
    int firstSize = first.size(); 
    int secondSize = second.size();
    if(firstSize > secondSize)
        return true;
    else if(firstSize < secondSize)
        return false;

    /* Convert to lower case, for case insentitive comprasion */
    std::transform(first.begin(), first.end(), first.begin(), ::tolower);
    std::transform(second.begin(), second.end(), second.begin(), ::tolower);

    /* Call the std::string operator>(...) which compare strings lexicographically */
    if(first > second)
        return true;

    /* In other cases first hex string is not greater */
    return false;
}
 
int main(int argc, char *argv[])
{
    string input;
    cin>>input;
    string target = "0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"; 
   
    
   string output;
   string test  = "1";
    
    int x = 0;
     while(true){
		 string input1 = input + to_string(x);
		 string output = sha256(input1);
		
		 if(hex_greater(target,output)){
			 cout<<output<<endl;
			 break;
		 }
		 
		 
		 x++;
		
	}
	
	
	
	
    return 0;
}
