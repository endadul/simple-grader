#include "stack.h"
#include <string>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[])
{
  string command, elem;
  Stack<int> intStack;
  int element;

  while(1){
    try{
      cout << "> " ; 
      if (!(cin >> command))
        break;
      if(command == "push"){
        cin >> elem;
        element = atoi (elem.c_str());
        intStack.push(element);
      }
      else if(command == "pop"){
        intStack.pop(element);
        cout << element << endl;
      }
      else if(command == "peek"){
        intStack.peek(element);
        cout << element << endl;
      }
      else if (command == "" || command.empty()){
        continue; // do nothing
      }
      else {
        cout << "Unknown command" << endl;
      }
    }
    catch(StackError &e)
    {
      cout << "Given command: " << command << endl;
      cout << e.what() << e.getMessage() << endl;
    }
  }
}
