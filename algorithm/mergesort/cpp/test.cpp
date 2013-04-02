#include <iostream>
#include <cstdlib>
#include <time.h>
#include <sys/time.h>
#include <fstream>
#include <cstring>
#include "sizeReader.h"
#include "rlist.h"
#include "ms.h"
#include "msPrinty.h"
#include "arrayPrinter.h"

using namespace std;

void msGraphTest();
void msTimeTest();
void msRandSortTest();
void randTest();
void msPrintyTest();

int main(int argc, char** argv){
	if (argc == 1){
		msRandSortTest();
	}
	else{
		if(argc == 2){
			if(argv[1][0] == 'g'){
				msGraphTest();
			}
			else if(argv[1][0] == 't'){
				msTimeTest();
			}
			else if(argv[1][0] == 'b'){
				msRandSortTest();
			}
			else if(argv[1][0] == 'r'){
				randTest();
			}
			else if(argv[1][0] == 'p'){
				msPrintyTest();
			}
			else{
				cout << "Unknown command :" << argv[1] << endl;
			}
		}
		else{
			cout << "Incorrect number of parameters :" << (argc-1) << ". Should be 1" << endl;
		}
	}
	return 0;
}

void msPrintyTest(){
	int size = getSize();
	int* pre = (int*)malloc(sizeof(int)*size);
	int i;
	for(i=0;i<size;i++){
		pre[i] = size-i-1;
	}
	msPrinty(pre,size,pre,size);
	printArray(pre,size);
}

void msRandSortTest(){
	cout << "Random List Sort" << endl;
	int size = getSize();
	int* rand = rlist(size);
	printArray(rand,size);
	ms(rand,size);
	printArray(rand,size);
}

void randTest(){
	cout << "Random Test" << endl;
	int size = getSize();
	int* rand = rlist(size);
	printArray(rand,size);
}

void msGraphTest(){
	cout << "Graph Test" << endl;
	int start;
	int end;
	int interval;
	int wait;
	int user;

	ifstream fin;
	string tmp;
	fin.open("../gcfg.txt");
	getline(fin,tmp);
	start = atoi(tmp.c_str());
	getline(fin,tmp);
	end = atoi(tmp.c_str());
	getline(fin,tmp);
	interval = atoi(tmp.c_str());
	getline(fin,tmp);
	wait = atoi(tmp.c_str());
	getline(fin,tmp);
	user = atoi(tmp.c_str());
	fin.close();

	int j, i;
	int* pre;
	int* exp;
	for(i=start;i<end;i+=interval){
		pre = (int*)malloc(sizeof(int)*i);
		for(j=0;j<i;j++){
			pre[j] = i-j-1;
		}
		struct timeval tim;
		gettimeofday(&tim,NULL);
		double startMilliTime = tim.tv_sec+(tim.tv_usec/1000000.0);
		time_t startTime = time(NULL);
		ms(pre,i);
		time_t endTime = time(NULL);
		gettimeofday(&tim,NULL);
		double endMilliTime = tim.tv_sec+(tim.tv_usec/1000000.0);
		if(user){
			cout << "took " << i << " " << endTime-startTime << " seconds to sort" << " (" << endMilliTime-startMilliTime << ")" << endl;
		}
		else{
			cout << i << ' ' << endTime-startTime << ' ' << endMilliTime-startMilliTime << endl;
		}
	}
	if(wait){
		int tmp;
		cin >> tmp;
		cout << tmp;
	}
}

void msTimeTest(){
	cout << "Time Test" << endl;
	int size;
	int write;
	int wait;
	int cr;
	char lend;

	ifstream fin;
	string tmp;
	fin.open("../cfg.txt");
	getline(fin,tmp);
	size = atoi(tmp.c_str());
	getline(fin,tmp);
	write = atoi(tmp.c_str());
	getline(fin,tmp);
	wait = atoi(tmp.c_str());
	getline(fin,tmp);
	cr = atoi(tmp.c_str());
	fin.close();
	cout << size << endl;

	int i;
	time_t prepStart = time(NULL);
	int* pre = (int*)malloc(sizeof(int)*size);
	int* exp = (int*)malloc(sizeof(int)*size);
	for(i=0;i<size;i++){
		pre[i] = size-i-1;
		exp[i] = i;
	}
	time_t prepEnd = time(NULL);

	time_t start = time(NULL);
	ms(pre,size);
	time_t end = time(NULL);

	time_t writeStart = time(NULL);
	if(cr){
		lend = '\n';
	}
	else{
		lend = ' ';
	}
	if(write){
		ofstream fout;
		fout.open("../lists-cpp.txt");
		for(i=0;i<size;i++){
			fout << pre[i] << lend;
		}
		if(!cr){
			fout << endl;
		}
		fout.close();
	}
	time_t writeEnd = time(NULL);
	cout << "prep " << prepEnd - prepStart << endl;
	cout << "toSort " << end-start << endl;
	cout << "write " << writeEnd - writeStart << endl;
	int T = true;
	for(i=0;i<size;i++){
		T = T && exp[i] == pre[i];
	}
	if(T){
		cout << "True" << endl;
	}
	else{
		cout << "False" << endl;
	}
	if(wait){
		int tmp;
		cin >> tmp;
		cout << tmp;
	}
}
