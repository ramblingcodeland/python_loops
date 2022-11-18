#include <stdio.h>
#include <time.h>
#define LOOP_COUNTER_MAX 100000001

int main(){

    clock_t start_time = clock();
    unsigned long acc = 0;
    for(unsigned long i=1; i < LOOP_COUNTER_MAX; i++) {
        acc += i;
    }
    clock_t end_time = clock();
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf(
        "\nElapsed time: %.6lf  Accumulator: %ld  - Pure C loop on gcc \n\n",
         elapsed_time, acc
    );

}