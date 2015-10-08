#include<stdio.h>

int main(){
	int a=0;
	int b=0;
	int c=0;

	int i,j,k;
	for(i=1;i<1000;i++){
		for(j=i;j<1000;j++){
			for(k=1;k<i+j && k<1000;k++){
				if(i+j+k==1000){
					if((i*i)+(j*j) == (k*k)){
						printf("%3d %3d %3d\n", i, j, k);
						printf("%d\n", i*j*k);
						return 0;
					}
				}
			}
		}
	}
	return 0;
}
