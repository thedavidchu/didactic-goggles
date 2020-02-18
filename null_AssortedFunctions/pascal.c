#include <stdio.h>
#include <stdlib.h>

int pascalIn(int, int***);
int pascalOut(int, int**);
int **pascal(int);

int main(void){
  int i=0, j=0;
  int n=0;
  int r=0;
  int **pIn=NULL;
  int **pOut=NULL;

  printf("How many Pascal Layers?");
  scanf("%d",&n);

  pOut=(int**)malloc(n*sizeof(int*));
  r=pascalIn(n,pIn);
  r=pascalOut(n,&pOut);


  printf("pIn: \n\n");
  for(i=0;i<n;i++){
    for(j=0;j<n;j++){
      printf("%d",pIn[i][j]);
    }
    printf("\n");
  }
  return 0;
}

int pascalIn(int N, int ***out){
  int i=0;
  int layer=0;
  if(out==NULL){
    return -1;
  }else if(N<1){
    return -1;  
  }
  
  *out=(int**)malloc();
  if(N==1){
    
  }
  for(i=0;i<N;i++){
    }
  }
}


int pascalOut(int N, int **out){
  return 0;
}


int **pascal(int N){
  return NULL;
}

int adder()