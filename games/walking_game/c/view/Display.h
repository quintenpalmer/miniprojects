#ifndef _DISPLAY_
#define _DISPLAY_
#include "../model/Model.h"

void display(Model* model);
void initDisplay(Model* model);
void emptyBoard(int width, int height, char* outBoard);
void displayEmptyBoard(int width, int height);
void printOutBoard(int width, int height, char* outBoard);
#endif
