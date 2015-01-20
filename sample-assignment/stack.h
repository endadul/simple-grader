#ifndef __STACK_H_
#define __STACK_H_
#include<iostream>
#include<string>
//#include<exception>
#include<stdexcept>
using namespace std;

template <class T>
class Stack
{
  protected:
    typedef struct Node{
      struct Node *next;
      T data;
    }Node;
    
    Node *top;
    bool isEmpty();

  public:
    Stack();
    virtual ~Stack();
    void push(T data);
    void pop(T& data);
    void peek(T& data);
};

class StackError : public runtime_error
{
  private:
    string msg;
  public:
    enum error_type {E_EMPTY = 0, E_FULL = 1};
    StackError(enum error_type t): runtime_error("Invalid operation: ")
    {
      msg = "Stack ";
      msg += (t == E_EMPTY ? "Empty" : "Full");
    }
    const char *getMessage(){ return msg.c_str();}
    ~StackError() throw() {}
};

template <class T>
Stack<T>::Stack()
{
  top = NULL;
}

template <class T>
Stack<T>::~Stack()
{
  Node *temp;
  while(top)
  {
    temp = top->next;
    delete top;
    top = temp;
  }
}

template <class T>
void Stack<T>::push(T data)
{
  Node *node = new Node;
  node->next = top;
  node->data = data;
  top = node;
  return;
}


template <class T>
void Stack<T>::pop(T& data)
{
  Node *temp = top;
  if(top == NULL)
  {
    throw StackError(StackError::E_EMPTY); 
  }

  data = top->data;
  top = top->next;
  delete temp;
}

template <class T>
void Stack<T>::peek(T& data)
{
  if(top == NULL)
  {
    throw StackError(StackError::E_EMPTY); 
  }
  data = top->data;
}

#endif // __STACK_H
