#include <stdio.h>

int reverse(int n)
{
    int r = n % 10;
    while ((n /= 10) > 0) {
        r *= 10;
        r += (n % 10);
    }
    return r;
}

int allodddigits(int n)
{
    while (n > 0) {
        if ((n % 10) % 2 == 0) {
            return 0;
        }
        n /= 10;
    }
    return 1;
}

int main(int argc, char **argv)
{
    int c = 0;
    for (int i = 0; i < 1000000000; i++) {
        if (i % 10 == 0) {
            continue;
        }
        if (allodddigits(i + reverse(i))) {
            c++;
            printf("%d %d\n", i, c);
        }
    }
    return 0;
}
