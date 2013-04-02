#include <stdlib.h>
#include "Player.h"
#include "Dir.h"
#include "Loc.h"

Player* newPlayer(char newName){
	Player* p = malloc(sizeof(Player));
	p->name = newName;
	p->dir = dleft;
	p->loc = newLoc(0,0);
	return p;
}

void face(Player* player, int newDir){
	player->dir = newDir;
}

void move(Player* player, int mDir, int amount){
	int x = 0;
	int y = 0;
	if(mDir==dright){
		x = amount;
	}
	else if(mDir==dup){
		y = amount;
	}
	else if(mDir==dleft){
		x = -amount;
	}
	else if(mDir==ddown){
		y = -amount;
	}
	moveLoc(player->loc,x,y);
}
