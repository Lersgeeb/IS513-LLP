//Comement by Line
/*
gcc factorialCpp.cpp -lstdc++ -o factorialCpp.o
Comment multiple line

*/

#include <iostream>
using namespace std;

int factorial(int n);

int main(){
	int n = factorial(5);
	cout<<"El factorial de 5 es: "<<n<<endl;
}
	
int factorial(int n){
	if(n<2)
		return 1;
	return n*factorial(n-1);
}
