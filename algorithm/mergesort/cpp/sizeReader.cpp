#include <cstdlib>
#include <fstream>
#include <cstring>
#include "sizeReader.h"
using namespace std;
int getSize(){
	int size;
	string tmp;
	ifstream fin;
	fin.open("../size.txt");
	getline(fin,tmp);
	size = atoi(tmp.c_str());
	return size;
}
