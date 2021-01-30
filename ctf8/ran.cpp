#include <iostream>
#include <ctime>
#include <stdlib.h>


int main(){
	srand((uint)time(NULL));
	std::cout << rand();
	return 0;
}

