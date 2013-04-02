#include "arrayPrinter.h"
#include <iostream>
using namespace std;
void printArray(int* array, int size){
	int i=0;
	for(i=0;i<size;i++){
		cout << array[i] << ' ';
	}
	cout << endl;
}
void pprintArray(int* array, int size){
	int i=0;
	int j=0;
	if(array[i]!=0){
		cout << 0;
		for(j=0;j<array[i]-1;j++){
			cout << "  ";
		}
		cout << ' ';
	}
	for(i=0;i<size-1;i++){
		cout << array[i];
		for(j=array[i];j<array[i+1]-1;j++){
			cout << "  ";
		}
		cout << ' ';
	}
	cout << array[size-1];
	cout << endl;
}
