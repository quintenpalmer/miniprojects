#ifndef _LOC_
#define _LOC_

typedef struct {
	int x;
	int y;
} Loc;

Loc* newLoc(int nX, int nY);

void moveLoc(Loc* l, int dX, int dY);
#endif
