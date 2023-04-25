#include<iostream>
#include<stdlib.h>
#include<vector>
#include<sstream>
#include<stack>
using namespace std;

struct node
{
  int key;
  bool clicker;
  node *parent;
  node *left;
  node *right;
};

class BinaryTree
{
    node *root;
    void inorder(node* nd);
    node* insert(int number, node* rt);
    bool search(int number, node* rt);
    node* search2(int number, node* rt);
    void preorder(node* rt);
    void postorder(node* rt);
    node* mintree(node* rt);
    void transplant(node* u, node* v);
    void treedelete(int number, node* rt);
    void clean(node* rt);
    node* maxtree(node* rt);
    node* postorder2(node* rt, int number);
    node* predecessor(node* root);

public :
        BinaryTree(){root = NULL;}
        ~BinaryTree(){clean(root);}
        void insert(int number){root = insert(number, root);}
        void displayInorder()
        {
            if(root != NULL)
            {
                inorder(root);
            }
            else cout<<"Error inorder";
        }
        void displayPreorder()
        {
            if(root != NULL)
            {
                preorder(root);
            }
            else cout<<"Error preorder";
        }
        void displayPostorder()
        {
            if(root != NULL)postorder(root);
            else cout<<"Error postorder";
        }
        void displaySearch(int number)
        {
            if(search(number, root)==true) cout << "True";
            else cout << "False";
            if(root == NULL) cout << "Error search";
        }
        void displayMinTree(){cout << mintree(root)->key;}
        void runDelete(int number)                
        {
            if(root != NULL and search(number, root) == true)treedelete(number, root);
            else cout<<"Error delete"<<endl;
        }
};

node*  BinaryTree::predecessor(node* rt) 
{
  if (!rt) return NULL;
    rt = rt->left;
  while (rt->right) rt = rt->right;
  return rt;
}

void BinaryTree::treedelete(int number, node* rt)
{
    node* temp = search2(number, rt);                            

    if(temp->left == NULL)
    {
        if(temp == root)root = temp->right;        
        transplant(temp, temp->right); 
        delete temp; 
    }
    else if(temp->right == NULL)
    {
        if(temp == root)root = temp->left;         
        transplant(temp, temp->left);
        delete temp; 
    }
    else
    {
        node* y = predecessor(temp);
        if(y->parent != temp)
        {
                transplant(y, y->left);
                y->left = temp->left;
                y->left->parent = y;
        }
        if(temp == root)root = y;       
        transplant(temp, y);
        y->right = temp->right;
        y->right->parent = y;
        delete temp;
    }
}

void BinaryTree::transplant(node* u,node* v)
{
        if(u->parent == NULL)
        {
            root = v;
        }
        else if(u == u->parent->left)
        {
            u->parent->left = v;
        }
        else
        {
            u->parent->right = v;
        }
        if(v != NULL)
            v->parent = u->parent;
}

node* BinaryTree::mintree(node* rt)
{
    while(rt->left != NULL)
    {
        rt = rt->left;
    }
    return rt;
}

node* BinaryTree::maxtree(node* rt) 
    {
        if(rt == NULL)
            return NULL;
        else if(rt->right == NULL)
            return rt;
        else
            return maxtree(rt->right);
    }

node* BinaryTree::insert(int number, node* rt)
{
    node *temp;
    temp = new node;
    temp->key = number;
    temp->left = temp->right = temp->parent = NULL;
    temp->clicker = true;
    node *x = rt;
    node *y = NULL;
    while(x != NULL)
    {
            y = x;
            if(temp->key < x->key)
            {
                x->clicker = !x->clicker;
                x = x->left;
            }
            else if(temp->key > x->key)
            {
                x->clicker = !x->clicker;
                x = x->right;
            }
            else if(temp->key == x->key)
            {
                x->clicker = !x->clicker;
                if(x->clicker == false) x = x->left;
                else x = x->right;
            }
    }
    temp->parent = y;    
    if(y == NULL)
    {
        rt = temp;
    }
    else if (temp->key < y->key)
    {
        y->left = temp;
    }
    else
    {
        y->right = temp;
    }
    return rt;
}

void BinaryTree::inorder(node* nd)
{
    if(nd != NULL)
    {
        inorder(nd->left);
        cout << nd->key;
        if(maxtree(root)!=nd) cout << " ";
        inorder(nd->right);
    }
}

void BinaryTree::preorder(node* nd)
{
    if(nd != NULL)
    {
        if(nd->parent != NULL and (maxtree(root) != nd or maxtree(root)->left != nd))cout << " ";        
        cout << nd->key;
        preorder(nd->left);
        preorder(nd->right);
    }
}

void BinaryTree::postorder(node* nd)
{
    if(nd != NULL)
    {
        postorder(nd->left);
        postorder(nd->right);
        cout << nd->key;
        if(nd->parent != NULL) cout << " ";         
    }
}

node* BinaryTree::postorder2(node* nd, int number)
{
    node* r = NULL;
    node* l = NULL;
    if(nd != NULL)
    {
        l = postorder2(nd->left, number);
        r = postorder2(nd->right, number);        
    }
    else return NULL;
    if(nd->key == number and r == NULL and l == NULL) return nd;
    else if(l != NULL) return l;
    return r; 
}

bool BinaryTree::search(int number, node* rt)
{
    if(rt == NULL)
        return false;
    else if(number < rt->key)
        return search(number, rt->left);
    else if(number > rt->key)
        return search(number, rt->right);
    else
        return true;
}

node* BinaryTree::search2(int number, node* rt)
{
    if(rt == NULL)
    {
        cout << "Error delete";
        return NULL;
    }
    else if(number < rt->key)
    {
        rt->clicker = !rt->clicker;
        return search2(number, rt->left);
    }
    else if(number > rt->key)
    {
        rt->clicker = !rt->clicker;
        return search2(number, rt->right);
    }
    else if(number == rt->key)
    {
        bool l = search(number, rt->left);
        bool r = search(number, rt->right);
        if(l == true and r == true)                 
        {
            node* finale = postorder2(rt, number);
            node* temp = finale->parent;
            while(temp != NULL)
            {
                temp->clicker = !temp->clicker;
                temp = temp->parent;
            }
            return finale;
        }
        else if(l == true and r == false)
        {
            rt->clicker = !rt->clicker;
            return search2(number, rt->left);
        }
        else if(r == true and l == false)
        {
            rt->clicker = !rt->clicker;
            return search2(number, rt->right);            
        }
        else return rt;
    }
    return rt;
}

void BinaryTree::clean(node* rt)
{
  if (rt != NULL) 
  {
    clean(rt->left);
    clean(rt->right);
  }
  delete rt;
}

int main()
{
    int x;
    vector <string> tab;
    string option;

    while(cin >> option)
    {
        tab.push_back(option);
    }
    for(unsigned long long int i = 0; i < tab.size(); i++)
    {
        if(tab[i] == "insert") cout << "Error insert";
        else if(tab[i] == "delete"){ cout << "Error delete"; i++;}
        else if(tab[i] == "search"){cout << "Error search"; i++;}
        else if(tab[i] == "in_order"){cout << "Error in_order";}
        else if(tab[i] == "pre_order"){cout << "Error pre_order"<<endl;}
        else if(tab[i] == "post_order"){cout << "Error post_order";}
        else if(tab[i] == "insert"){cout << "Error insert";i++;}
        else if(tab[i] == "init_tree") 
        {
            BinaryTree* tree = new BinaryTree;

            for(unsigned long long int y = i; y < tab.size(); y++ )
            {
                if(tab[y] == "insert")
                {
                        istringstream iss(tab[y+1]);
                        iss>> x;
                        tree->insert(x);
                        y++;
                }
                else if(tab[y] == "in_order")
                {
                        tree->displayInorder();
                        if(y+1 != tab.size()) cout<<"\n";
                }
                else if(tab[y] == "pre_order")
                {
                        tree->displayPreorder();
                        if(y+1 != tab.size()) cout<<"\n";
                }
                else if(tab[y] == "post_order")
                {
                        tree->displayPostorder();
                        if(y+1 != tab.size()) cout<<"\n";
                }
                else if(tab[y]=="search")
                {
                        istringstream iss(tab[y+1]);
                        iss >> x;
                        tree->displaySearch(x);
                        if(y+1 != tab.size()) cout<<"\n";
                        y++;
                } 
                else if(tab[y]=="delete") 
                {
                        istringstream iss(tab[y+1]);
                        iss >> x;
                        tree->runDelete(x);
                        y++;
                } 
            }

            delete tree;
            break;
        }
    }
      return 0;
}