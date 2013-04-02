#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int even_div(int num, int div){
	return fmod((float)num,(float)div) == 0.0;
}

int can_add(int num, int* array, int size){
	int i;
	int can = 1;
	for(i=0;i<size;i++){
		if(num == array[i]){
			can = 0;
		}
	}
	return can;
}

int find_sum(int* array, int size){
	int total = 0;
	int i;
	for(i=0;i<size;i++){
		total = total + array[i];
	}
	return total;
}


int find_even_divs(int num, int* even_divs){
	int div;
	int i;
	int current_index = 0;
	even_divs[current_index] = 1;
	current_index++;
	for(div=2;div<num;div++){
		if(even_div(num,div)){
			if(can_add((int)(num/div),even_divs,current_index)){
				even_divs[current_index] = (int)(num/div);
				current_index++;
			}
			if(can_add(div,even_divs,current_index)){
				even_divs[current_index] = div;
				current_index++;
			}
		}
	}
	return current_index;
}

int find_amis(int top){
	int sums[top];
	int i;
	int s;
	int count;
	int current_index = 0;
	int amis[top];
	int even_divs[100];
	for(i=0;i<top;i++){
		count = find_even_divs(i,even_divs);
		s = find_sum(even_divs,count);
		sums[i] = s;
	}
	for(i=0;i<top;i++){
		if(sums[i] < top && sums[i] > 0){
			if(sums[sums[i]] == i && i != sums[i]){
				amis[current_index] = i;
				current_index++;
			}
		}
	}
	return find_sum(amis,current_index);
}

int main(int argc, char** argv){
	int to_find = 10000;
	if(argc==2){
		to_find = atoi(argv[1]);
	}
	int start_time = time(NULL);
	int sum = find_amis(to_find);
	printf("%d\n",sum);
	printf("%d seconds\n",time(NULL)-start_time);
	return 0;
}
