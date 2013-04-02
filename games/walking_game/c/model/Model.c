#include <stdlib.h>
#include "Player.h"
#include "Board.h"
#include "Model.h"

Model* newModel(int nHeight, int nWidth){
	Model* m = malloc(sizeof(Model));
	m->board = newBoard(nHeight,nWidth);
	m->index=0;
	return m;
}

int getHeight(Model* model){
	return model->board->height;
}

int getWidth(Model* model){
	return model->board->width;
}

Player* addPlayer(Model* model, char c){
	Player* p = newPlayer(c);
	int tmp = model->index;
	model->index++;
	model->players[tmp] = p;
	return p;
}

Player* getPlayer(Model* model, int index){
	return model->players[index];
}
