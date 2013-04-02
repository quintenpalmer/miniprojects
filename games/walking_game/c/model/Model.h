#ifndef _MODEL_
#define _MODEL_
#include "Player.h"
#include "Board.h"

typedef struct {
	Board* board;
	Player* players[4];
	int index;
} Model;

Model* newModel(int nHeight, int nWidth);
int getHeight(Model* model);
int getWidth(Model* model);
Player* addPlayer(Model* model, char c);
Player* getPlayer(Model* model, int index);
#endif
