#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
	int a,b,add;
	a = atoi(argv[1]);
	b = atoi(argv[2]);
	add = a+b;

	printf("%d",add);
	return 0;
}