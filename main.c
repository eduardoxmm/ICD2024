#include <stdio.h>

int main(){
int h=0, m=0, s=0;
int reloj=1;
  do
  {
    {
      while(h<24){
        m=0;
        while(m<60){
          s=0;
          while(s<60){
            s=s+1;
            printf("%02d:%02d:%02d\n",h,m,s);
          }
          m=m+1;
          printf("%02d:%02d:%02d\n",h,m,s);
        }
        h=h+1;
        printf("%02d:%02d:%02d\n",h,m,s);
      }
    }
  }while(reloj==1);
return 0;
}
