#include <stdio.h>
#include <stdlib.h>

int* mystery(int length);
void printmystery(int length);

int main(int argc, char** argv){
	if(argc==2){
		printmystery(atoi(argv[1]));
	}
	else{
		printmystery(4);
	}
	return 0;
}

int sizeReq(int length){
	return 1 << length;
}

int* mystery(int length){
	int* outArray = malloc(sizeof(int)*sizeReq(length));
	outArray[0] = 0;
	int size = 1;
	int i, j;
	for(i=0;i<length;i++){
		int currSize = size;
		for(j=0;j<currSize;j++){
			outArray[size] = !outArray[j];
			size++;
		}
	}
	return outArray;
}

void printmystery(int length){
	int* mysteryarray = mystery(length);
	int i;
	for(i=0;i<sizeReq(length);i++){
		printf("%d",mysteryarray[i]);
	}
	printf("\n");
}
