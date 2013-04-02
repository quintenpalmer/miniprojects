#include <stdlib.h>
#include "Board.h"

Board* newBoard(int nHeight, int nWidth){
	Board* b = malloc(sizeof(Board));
	b->height=nHeight;
	b->width=nWidth;
	return b;
}
