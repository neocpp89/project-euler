#include <stdio.h>

int count_ps(int md, int cd, int late, int numabs)
{
    int c = 0;
    if (md == cd) {
        return 1;
    }

    if (late == 0) {
        c += count_ps(md, cd+1, late+1, 0);
    }

    if (numabs < 2) {
        c += count_ps(md, cd+1, late, numabs+1);
    }

    c += count_ps(md, cd+1, late, 0);
    return c;
}

int main(int argc, char **argv)
{
    printf("%d\n", count_ps(30, 0, 0, 0));
    return 0;
}
