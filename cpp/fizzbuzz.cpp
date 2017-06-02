#include <iostream>
#include <vector>
using namespace std;

vector <string> FizzBuzz(int start,int end)
{
    std::vector<std::string> res;
    int j;
    res.resize(1+end-start);
    for (int i=start; i<=end; i++)
    {
        j=i-start;
        if (i%15==0)
            res[j]="FizzBuzz";
        else if (i%5==0)
            res[j]="Fizz";
        else if (i%3==0)
            res[j]="Buzz";
        else
            res[j]=std::to_string(i);
    }
    return res;
}
int main(){
    //ofstream fout();
    std::vector<string> res;
    int _start=5;
    int _end=15;
    res=FizzBuzz(_start,_end);
    for (int res_i=0; res_i<res.size(); res_i++){
        cout<<res[res_i]<<endl;
    }
    return 0;
}
