/*
init_stack 
push 1 
push 2 
push 3 
push 4 
push 5 
push 6 
push 7 
push 8 
push 9 
push 10 
peek 
pop 
peek 
pop 
peek 
pop 
peek 
pop 
peek 
pop 
peek 
pop 
peek 
pop 
peek 
pop 
peek
pop 
peek 
pop 
empty
*/
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<sstream>

using namespace std;

struct node
{
  int data;
  node *next;
};

class stack
{
      node *top;
      node *first;
public :
      stack()
      { top=NULL;}
       void push(int add);
       void pop();
       void peek();
       void search(int sought);
       void empty();
      ~stack();
};

void stack::push(int add)
{
      node *check=top;
      if(check==NULL)
      {
            node *temp;
            temp=new node;
            temp->data=add;
            temp->next=top;
            top=temp;
            first=temp;  
      }
      else
      {
            node *temp;
            temp=new node;
            temp->data=add;
            temp->next=top;
            top=temp; 
      }
}

void stack::pop()
{
      if(top!=NULL)
      {
            node *temp=top;
            top=top->next;
            delete temp;
      }
      else
            cout<<"Error pop"<<endl;
}

void stack::peek()
{
      if(top!=NULL)
      {
            node *temp=top;
            cout<<temp->data;
      }
      else
            cout<<"Error peek"<<endl;
}

void stack::search(int sought)
{
      if(top!=NULL)
      {
            node *temp=top;
            node *check=first;
            do
            {
                  if(temp->data==sought)
                  {
                        cout<<"True";
                        return;
                  }
                  else if(temp->data==check->data)
                  {
                        cout<<"False";
                        return;
                  }
                  temp=temp->next;
            }while(temp->data!=check->data&&temp->next!=check->next);
            if(check->data==sought)
            {
                  cout<<"True";
                  return;
            }
            else
            {
                  cout<<"False";
                  return;
            }
      }
      else
      {
            cout<<"Error search";
      }
}

void stack::empty()
{
      node *temp=top;
      if(top==NULL) cout<<"True";
      else cout<<"False";
}

stack::~stack()
{
      while(top!=NULL)
      {
            node *temp=top;
            top=top->next;
            delete temp;
      }
}

int main()
{     
      int x;
      vector <string> tab;
      string option;
      while(cin>>option)
      {
            tab.push_back(option);
      }

      if(tab[0]=="init_stack") {
            stack st;
            for( int i = 1; i < tab.size(); i++ )
            {
                        if(tab[i]=="push")
                        {
                              istringstream iss(tab[i+1]);
                              iss>> x;
                              st.push(x);
                              i++;
                        }
                        else if(tab[i]=="search")
                        {
                              istringstream iss(tab[i+1]);
                              iss>> x;
                              st.search(x);
                              if(i+1 != tab.size()) cout<<"\n";
                              i++;
                        } 
                        else if(tab[i]=="peek")
                        {
                              st.peek();
                              if(i+1 != tab.size()) cout<<"\n";
                        }
                        else if(tab[i]=="empty"){
                        st.empty();
                        if(i+1 != tab.size()) cout<<"\n";
                        }
                        else if(tab[i]=="pop") st.pop();

            }
            st.~stack();
      }
      else
      {
            cout<<"Error init_stack";
      }
      return 0;
}