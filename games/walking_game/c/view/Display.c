#include <stdio.h>
#include "../model/Model.h"
#include "Display.h"

void display(Model* model){
	int i=0;
	int j=0;
	int width = getWidth(model);
	int height = getHeight(model);
	for(i=0;i<height;i++){
		printf("\e[A");
	}
	char outBoard[width*height];
	emptyBoard(width,height,outBoard);
	Player* player;
	for(i=0;i<model->index;i++){
		player = getPlayer(model,i);
		outBoard[player->loc->x+player->loc->y*width] = player->name;
	}
	printOutBoard(width,height,outBoard);
}

void initDisplay(Model* model){
	displayEmptyBoard(getWidth(model),getHeight(model));
}

void emptyBoard(int width, int height, char* outBoard){
	int i=0;
	int j=0;
	for(i=0;i<height;i++){
		for(j=0;j<width;j++){
			outBoard[j+i*width] = '.';
		}
	}
}

void displayEmptyBoard(int width, int height){
	char outBoard[width*height];
	emptyBoard(width,height,outBoard);
	printOutBoard(width,height,outBoard);
}

void printOutBoard(int width, int height, char* outBoard){
	int i=0;
	int j=0;
	for(i=height-1;i>=0;i--){
		printf("\r");
		for(j=0;j<width;j++){
			printf("%c",outBoard[j+i*width]);
		}
		printf("\r\n");
	}
}
