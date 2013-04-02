#include <stdio.h>
#include <stdlib.h>

//typedef unsigned long long big;
typedef long big;

big fib(int nth){
	big curr = 1LL;
	big old = 0LL;
	big tmp;
	int index;
	for(index=0;index<nth;index++){
		tmp = curr;
		curr = curr + old;
		old = tmp;
	}
	return curr;
}

int main(int argc, char** argv){
	int nth = 13;
	if(argc==2){
		nth = atoi(argv[1]);
	}
	//printf("size of big is %d\n",sizeof(big));
	printf("fib of %d is %ld\n",nth,fib(nth));
	return 0;
}
