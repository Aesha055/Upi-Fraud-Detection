#include<bits/stdc++.h>
using namespace std ;
struct  Node 
{
 int data;
 Node *next;
    /* data */
};
Node ( int data1 ,Node* next1  )
{
     data= data1 ;
    next= next1  ;

}
int main 
{ vector <int> arr= {3,2,4,1};
 Node *y = new Node( arr[0],nullptr);




    return 0;
}