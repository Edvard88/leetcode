
// Simple C++ program to display "Hello World"
 
// Header file for input output functions
#include<iostream>
 
using namespace std;
 

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        
        vector<int> resultArray;
        //int len = nums.size();
        //vector<int> resultArray[len]={};
        
        //int resultArray[len]={};
        
                    
        for(int i=0; i<nums.size(); i++){
            resultArray.push_back(nums[nums[i]]);
            
        };
     return resultArray;   
        
    }
}
     

int main()
{   

    vector<int> nums {0,2,1,5,3,4};
    solution = Solution();

    result = solution.buildArray(solution);
    // prints hello world
    cout<<"Result: "<<result<<endl;

       
    return 0;
}
