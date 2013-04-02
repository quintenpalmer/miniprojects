#ifndef _BOARD_
#define _BOARD_

typedef struct {
	int height;
	int width;
} Board;

Board* newBoard(int nHeight, int nWidth);
#endif
