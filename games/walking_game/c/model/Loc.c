#include <stdlib.h>
#include "Loc.h"

Loc* newLoc(int nX, int nY){
	Loc* l = malloc(sizeof(Loc));
	l->x = nX;
	l->y = nY;
	return l;
}

void moveLoc(Loc* l, int dX, int dY){
	l->x += dX;
	l->y += dY;
}
