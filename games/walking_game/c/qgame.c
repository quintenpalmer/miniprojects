#include "model/Model.h"
#include "control/Control.h"

int main(int argc, char** argv){
	int height= 20;
	int width = 30;
	Model* model = newModel(height,width);
	Player* p1 = addPlayer(model,'q');
	Player* p2 = addPlayer(model,'d');
	initDisplay(model);
	mainLoop(model);
	return 1;
}
