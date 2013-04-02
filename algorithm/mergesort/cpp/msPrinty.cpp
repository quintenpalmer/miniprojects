#include <cstdlib>
#include <cstring>
#include "arrayPrinter.h"
#include "msPrinty.h"

void msPrinty(int* array, int size, int* root, int rootSize){
	if(size>2){
		int lhsize = size/2;
		int rhsize = size-size/2;
		printArray(root,rootSize);
		msPrinty(&array[0],lhsize,root,rootSize);
		printArray(root,rootSize);
		msPrinty(&array[size/2],rhsize,root,rootSize);
		printArray(root,rootSize);
		int *tlh = &array[0];
		int *trh = &array[size/2];
		int *lh = (int*)malloc(sizeof(int)*lhsize);
		int *rh = (int*)malloc(sizeof(int)*rhsize);
		int *rlh = lh;
		int *rrh = rh;

		memcpy(lh,tlh,sizeof(int)*lhsize);
		memcpy(rh,trh,sizeof(int)*rhsize);

		int i, j;
		for(j=0;j<size;j++){
			if(lhsize==0 || ( rhsize>0 && lh[0] > rh[0] )){
				array[j] = rh[0];
				rh++;
				rhsize--;
			}
			else{
				array[j] = lh[0];
				lh++;
				lhsize--;
			}
		}
		printArray(root,rootSize);
		lh = rlh;
		rh = rrh;
		free(lh);
		free(rh);
	}
	else if(size==2 && array[0] > array[1]){
		int tmp = array[0];
		array[0] = array[1];
		array[1] = tmp;
	}
}
