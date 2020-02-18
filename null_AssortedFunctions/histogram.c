#include <stdio.h>
#include <stdlib.h>

int histogram(int*, struct entry*, int);
int fibo(int); /*fibo_three*/

struct entry{
	int valid;
	int value;
	int frequency;
};

int main(void){
	int i=0, r=0;
	int n[100];
	struct entry m[100];
	for(i=0;i<100;i++){
		(m[i]).valid=0;
		n[i]=i;
	}
	n[99]=98;
	r=histogram(n,m,100);
	printf("%d",r);
	/*print tests and other stuff*/
}

/*1*/
int average(float* array, float *output, int size){
	int i=0;
	float sum=0;
	if(array==NULL || output==NULL ||size<0 ){
		return -1;
	}else{
		output=(float*)malloc(sizeof(float));
		for(i=0;i<size;i++){
			sum=sum+array[i];
		}
		*output=sum/n;
		return 0;
	}
}

/*8a*/
struct term{
	float coef;
	float power;
	struct term *next;
};

typedef struct term term;

/*8b*/
int integrate(term *poly){
	term *point=NULL;
	if(poly==NULL){
		return -1;
	}else{
		point=poly;
		while(point != NULL){
			point->power=power+1;
			point->coef=coef/power;
			point=point->next;
		}
		return 0;
	}
}

/*9*/


/*10*/
int nsum(float *a, float *b, int n, float *output){
	/*Consider a function in C called nsum that has four arguments:
a (an input vector), b (another input vector), n and output. It should
compute an output vector that contains the vector sum of a and b. To
handle general numbers, what should the types of a and b be (3 points)?
What is the purpose of n, and what is its type (2 points)? Assuming
the caller did not allocate output, what is the type of output (3 points)?
Write this function (12 points)*/
	if(*output==NULL || n==0){
		return -1;
	}else{
		output=(float*)malloc(n*sizeof(float));
		for(i=0;i<n;i++){
			output[i]=a[i] +b[i];
		}
	return 0;
	}
}

/*11*/
int isPrime(int n){
	int i=0;
	if(n<2){
		return -1;
	}else{
		for(i=2;i<n;i++){
			if(n % i == 0){
				return 0;
		}
		return -1;
	}
}

int isPrimeProduct(int n){
	int i=0;
	if(n<4){
		return -1;
	}else{
		for(i=2;i<n;i++){
			if(isPrime(i)==0 && n % i ==0){
				return 0;
			}
		}
		return -1;
	}
}

/*12*/
int histogram(int *n, struct entry *m, int s){
	int i=0, j=0;
	if(n==NULL || m==NULL || s==0){
		return -1;
	}
	for(i=0;i<s;i++){
		found=0;
		for(j=0;j<s;j++){
			if((m[j]).valid==1){
				if((m[j].value==n[i]){
					(m[j]).frequency (m[j]).frequency +1;
					found=1;
				}else{
					break /*Why??? Shouldn't it just keep going?*/
				}
			}else{
				m[j].valid=1;
				m[j].value=n[i];
				m[j].frequency=1;
			}
		}
	}
	return 0;
}

/*13*/
int getmode(struct entry *m, int *mode){
	int i=0, *mode=NULL, freq=0;
	if(m==NULL){
		return -1;
	}else{
		while((m[i]).valid != 0){
			if((m[i]).frequency>freq){
				freq=(m[i]).frequency
			}
			i++;
		}
		return 0;
	}
}

/*14*/
int fibo(int n){ /*fibo_three*/
	if(n==0 || n==1 || n==2){
		return 1;
	}else{
		return fibo(n-1) + fibo(n-2) + fibo(n-3);
	}
}

