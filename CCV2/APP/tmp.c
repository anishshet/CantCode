#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main(int argc, char *argv[]){
    char hello_world[] = "Hello World! ";
    char * result = (char *)malloc(sizeof(char)*100);
    strcat(result,hello_world);
    strcat(result,argv[1]);
    printf("%s\n",result);
    return 0;
}
