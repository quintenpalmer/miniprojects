#include <stdio.h>
#include <unistd.h>

int main(){
	FILE *fp;
	fp=fopen("../settings.txt","r");
	int num;
	int wait;
	fscanf(fp,"%d\n%d\n",&num,&wait);
	int i;
	for(i=0;i<=num;i++){
		printf("\r%d\%%  ",i);
		fflush(stdout);
		usleep(wait*1000);
	}
	printf("\n");
	return 0;
}
