// Online C compiler to run C program online
#include <stdio.h>
#include <pthread.h>

#define MAXTHREADS 1

int sum;

typedef struct {
    int i;
    int j;
} thread_arg_t;

void * thread_add(void * t_arg) {
    thread_arg_t * arg = t_arg;
    for (int i=arg->i; i < arg->j; i++) {
        sum += i;
    }
    return NULL;
}

int main() {    
    // create the threads, args
    pthread_t threads[MAXTHREADS];
    thread_arg_t args[MAXTHREADS];
    int n = 100000;
    sum = 0;
    int rv;
    
    args[0].i=1;
    args[0].j=100000;
    
    rv = pthread_create(&threads[0], NULL, thread_add, &args[0]);
    if (rv < 0) {
        perror("Thread create error");
    }
    
    rv = pthread_join(threads[0], NULL);
    if (rv < 0) {
        perror("Thread join error");
    }

    // Compare the sums
    printf("Expected %d, Sum: %d\n", n*(n+1)/2, sum);
    assert(sum == n*(n+1)/2);
    
    return 0;
}
