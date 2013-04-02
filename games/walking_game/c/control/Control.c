#include <stdio.h>
#include "../model/Model.h"
#include "../view/Display.h"
#include "Control.h"

void mainLoop(Model* model){
	system("stty raw");
	char a = 'z';
	while(a != 'q'){
		Player* player;
		player = getPlayer(model,0);
		int dir = ddown;
		a = getchar();
		if(a=='d'){
			move(player,dright,1);
		}
		else if(a=='w'){
			move(player,dup,1);
		}
		else if(a=='a'){
			move(player,dleft,1);
		}
		else if(a=='s'){
			move(player,ddown,1);
		}
		else if(a=='D'){
			face(player,dright);
		}
		else if(a=='W'){
			face(player,dup);
		}
		else if(a=='A'){
			face(player,dleft);
		}
		else if(a=='S'){
			face(player,ddown);
		}
		player = getPlayer(model,1);
		if(a=='l'){
			move(player,dright,1);
		}
		else if(a=='i'){
			move(player,dup,1);
		}
		else if(a=='j'){
			move(player,dleft,1);
		}
		else if(a=='k'){
			move(player,ddown,1);
		}
		else if(a=='L'){
			face(player,dright);
		}
		else if(a=='I'){
			face(player,dup);
		}
		else if(a=='J'){
			face(player,dleft);
		}
		else if(a=='K'){
			face(player,ddown);
		}
		display(model);
	}
	system("stty sane");
}
