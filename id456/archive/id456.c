#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define IDX_X(n) (2*((n)))
#define IDX_Y(n) (2*((n))+1)

#define FIDX_X(n) (3*((n))+0)
#define FIDX_Y(n) (3*((n))+1)
#define FIDX_THETA(n) (3*((n))+2)

int ptcmp_angle(const void *a, const void * b)
{
    long double *ela = (long double *)a;
    long double *elb = (long double *)b;
    long double r = (ela[FIDX_THETA(0)] - elb[FIDX_THETA(0)]);

    if (r < 0) {
        return -1;
    } else if (r == 0) {
        return 0;
    } else {
        return 1;
    }
}

long double *verts_unit_circle_projection(int *verts, int num_vertices)
{
    long double *dverts;
    long double r, theta;
    int i;
    long double x, y;

    dverts = malloc(3 * sizeof(long double) * num_vertices);

    for (i = 0; i < num_vertices; i++) {
        x = (long double)verts[IDX_X(i)];
        y = (long double)verts[IDX_Y(i)];
        r = hypotl(x,y);
        theta = atan2l(y,x);
        if (r == 0) {
            dverts[FIDX_X(i)] = 0.0;
            dverts[FIDX_Y(i)] = 0.0;
            dverts[FIDX_THETA(i)] = 0.0;
        } else {
            dverts[FIDX_X(i)] = x / r;
            dverts[FIDX_Y(i)] = y / r;
            dverts[FIDX_THETA(i)] = theta + M_PI; /* theta range from [0,2pi) */
        }
    }

    /* sort by angle */
    qsort(dverts, num_vertices, 3 * sizeof(long double), ptcmp_angle);

    return dverts;
}

int idx_nn_theta_less_than(long double theta_max, long double *dverts, int num_vertices)
{
    size_t imin;
    size_t imax;
    size_t imid;

    imin = -1;
    imax = num_vertices;

    /* quick checks */
/*    if (theta_max > dverts[FIDX_THETA(num_vertices-1)])*/
/*        return num_vertices-1;*/
/*    if (theta_max < dverts[FIDX_THETA(0)])*/
/*        return -1;*/

    while ((imax - imin) > 1) {
        imid = imin + (imax - imin) / 2;
        if (dverts[FIDX_THETA(imid)] > theta_max) {
            imax = imid;
        } else {
            imin = imid;
        }
    }

    return imin;
}

long double angle_diff(long double a, long double b)
{
    long double diff = a - b;
    while (diff < 0) diff += 2.0*M_PI;
    while (diff >= 2.0 * M_PI) diff -= 2.0*M_PI;
    return diff;
}

int *generate_n_yk(long double *ucverts, int num_vertices)
{
    int *n_yk_array;
    int i;
    int j;
    long double current_theta;

    n_yk_array = (int *)malloc(sizeof(int) * num_vertices);

    /* assume first angle is <= pi! */
    current_theta = ucverts[FIDX_THETA(0)];
    n_yk_array[0] = idx_nn_theta_less_than(current_theta + M_PI, ucverts, num_vertices);

    for (i = 1; i < num_vertices; i++) {
        current_theta = ucverts[FIDX_THETA(i)];
        n_yk_array[i] = n_yk_array[i-1];
        while (angle_diff(ucverts[FIDX_THETA((i + n_yk_array[i]) % num_vertices)], current_theta) <= M_PI) {
            n_yk_array[i]++;
        }
        while (angle_diff(ucverts[FIDX_THETA((i + n_yk_array[i]) % num_vertices)], current_theta) > M_PI) {
            n_yk_array[i]--;
        }
    }

    return n_yk_array;
}

int *read_vertices(char *filename, int num_vertices)
{
    FILE *f;
    int *verts;
    int i;

    f = fopen(filename, "r");

    /* each vert has contiguous x,y components */
    verts = (int *)malloc(2 * sizeof(int) * num_vertices);

    for(i = 0; i < num_vertices; i++) {
        fscanf(f, "%d,%d", &verts[IDX_X(i)], &verts[IDX_Y(i)]);
    }
    return verts;
}

int main(int argc, char **argv)
{
    int *verts;
    int *n_yk;
    long double *unit_circle_verts;
    int num_vertices = 2000000;
/*    int num_vertices = 40000;*/
/*    int num_vertices = 600;*/
/*    int num_vertices = 8;*/
    int i,j,k;
    unsigned long long nv = (unsigned long long)num_vertices + 1;
    unsigned long long counter = ((2 * nv - 3) * (nv - 1) * (nv - 2)) / 6;
    printf("nv = %llu\n", nv);

    char vertfilename[255];
    sprintf(vertfilename, "vertices_%d.txt", num_vertices);
    
    verts = read_vertices(vertfilename, num_vertices);
    unit_circle_verts = verts_unit_circle_projection(verts, num_vertices);
/*    for(i = 0; i < num_vertices; i++) {*/
/*        printf("theta=%g,x=%g,y=%g\n", unit_circle_verts[FIDX_THETA(i)], unit_circle_verts[FIDX_X(i)], unit_circle_verts[FIDX_Y(i)]);*/
/*    }*/
    printf("Done reading vertices.\n");
    n_yk = generate_n_yk(unit_circle_verts, num_vertices);
/*    for(i = 0; i < num_vertices; i++) {*/
/*        printf("n[y_%d]=%d\n", i, n_yk[i]);*/
/*    }*/
    printf("Done generating n_yk.\n");

    printf("Counter initialized to %lu.\n", counter);
    unsigned long long *nyk_sq = (unsigned long long *)malloc(sizeof(unsigned long long) * num_vertices);
    for (i = 0; i < num_vertices; i++) {
        nyk_sq[i] = (unsigned long long)n_yk[i] * (unsigned long long)n_yk[i];
        counter -= nyk_sq[i];
/*        printf("\r%d/%d", i, num_vertices);*/
/*        fflush(stdout);*/
    }
    counter /= 2;
    printf("\nDone, counter=%llu.\n", counter);

    return 0;
}
