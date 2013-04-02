#include <cstdlib>
#include <sys/time.h>
#include "rlist.h"
int* rlist(int size){
	struct timeval tim;
	gettimeofday(&tim,NULL);
	srand(tim.tv_usec);
	int* a = (int*)malloc(sizeof(int)*size);
	int* b = (int*)malloc(sizeof(int)*size);
	int i, j, r;
	for(i=0;i<size;i++){
		a[i] = i;
	}
	for(i=0;i<size;i++){
		r = rand() % (size-i);
		b[i] = a[r];
		for(j=r;j<size;j++){
			a[j] = a[j+1];
		}
	}
	return b;
}
