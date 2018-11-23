#include <stdio.h>
#include <stdlib.h>

int fibo_three(int);

int main(void){
  int i=0;
  for(i=0;i<20;i++){
    printf("%d\n",fibo_three(i));
  }
}

int fibo_three(int n){
  if(n<0){
    return -1;
  }else if(n==0 || n==1 || n==2){
    return 1;
  }else{
    return fibo_three(n-1) + fibo_three(n-2) + fibo_three(n-3);
  }
}
