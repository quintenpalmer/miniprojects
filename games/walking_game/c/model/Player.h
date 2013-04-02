#ifndef _PLAYER_
#define _PLAYER_
#include "Dir.h"
#include "Loc.h"

typedef struct {
	char name;
	int dir;
	Loc* loc;
} Player;

Player* newPlayer(char newName);
void face(Player* player, int newDir);
void move(Player* player, int mDir, int amount);
#endif
