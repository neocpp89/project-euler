#include <stdio.h>
#include "dlx.h"

int ijn_to_index(int i, int j, int n)
{
    if (i < 0 || i > 8) {
        return -1;
    }
    if (j < 0 || j > 8) {
        return -1;
    }
    if (n < 1 || n > 9) {
        return -1;
    }
    return 9*9*i + 9*j + (n-1);
}

int ij_to_block(int i, int j)
{
    if (i < 0 || i > 8) {
        return -1;
    }
    if (j < 0 || j > 8) {
        return -1;
    }

    int rb = (i / 3);
    int cb = (j / 3);
    return (3*rb + cb);
}

int get_cel_constraint_column(int i, int j, int n)
{
    return 9*j + i;
}

int get_row_constraint_column(int i, int j, int n)
{
    return 81 + (9*i) + (n-1);
}

int get_col_constraint_column(int i, int j, int n)
{
    return 2*81 + (9*j) + (n-1);
}

int get_blk_constraint_column(int i, int j, int n)
{
    int blk = ij_to_block(i, j);
    return 3*81 + 9*blk + (n-1);
}


struct dlx_matrix *sudoku_matrix()
{
    struct dlx_matrix *m = dlx_matrix_create();
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            for (int n = 1; n <= 9; n++) {
                int row = ijn_to_index(i, j, n);
                dlx_matrix_insert(m, row, get_cel_constraint_column(i, j, n));
                dlx_matrix_insert(m, row, get_row_constraint_column(i, j, n));
                dlx_matrix_insert(m, row, get_col_constraint_column(i, j, n));
                dlx_matrix_insert(m, row, get_blk_constraint_column(i, j, n));
            }
        }
    }
    return m;
}

int main(int argc, char **argv)
{
    // struct dlx_matrix *m = dlx_matrix_create();

    // found this example at https://github.com/blynn/dlx
    // answer should be rows [3] or [0, 2]
    /*
    dlx_matrix_insert(m, 0, 0);
    dlx_matrix_insert(m, 0, 2);
    dlx_matrix_insert(m, 1, 1);
    dlx_matrix_insert(m, 1, 2);
    dlx_matrix_insert(m, 2, 1);
    dlx_matrix_insert(m, 3, 0);
    dlx_matrix_insert(m, 3, 1);
    dlx_set_optional(m, 2);

    int sel[100];
    dlx_search(m, 0, sel);
    */

    // Knuth's example
    // answer should be [0, 3, 4]
    /*
    dlx_matrix_insert(m, 0, 2);
    dlx_matrix_insert(m, 0, 4);
    dlx_matrix_insert(m, 0, 5);
    dlx_matrix_insert(m, 1, 0);
    dlx_matrix_insert(m, 1, 3);
    dlx_matrix_insert(m, 1, 6);
    dlx_matrix_insert(m, 2, 1);
    dlx_matrix_insert(m, 2, 2);
    dlx_matrix_insert(m, 2, 5);
    dlx_matrix_insert(m, 3, 0);
    dlx_matrix_insert(m, 3, 3);
    dlx_matrix_insert(m, 4, 1);
    dlx_matrix_insert(m, 4, 6);
    dlx_matrix_insert(m, 5, 3);
    dlx_matrix_insert(m, 5, 4);
    dlx_matrix_insert(m, 5, 6);
    */

    FILE *fp = fopen("p096_sudoku.txt", "r");

    const int kBufferSize = 256;
    char line[kBufferSize];

    while (1) {
        int row = -1;
        struct dlx_matrix *m = sudoku_matrix();
        int forced = 0;
        while (fgets(line, kBufferSize, fp) != NULL) {
            if (row == -1) {
                // skip header
                row++;
                continue;
            }

            // printf("%s", line);

            for (int col = 0; col < 9; col++) {
                int n = line[col] - '0';
                if (n != 0) {
                    dlx_matrix_insert(m, ijn_to_index(row,col,n), 4*81 + forced);
                    forced++;
                }
            }
            row++;
            if (row == 9) {
                break;
            }
        }

        if (row == -1) {
            dlx_matrix_delete(m);
            break;
        }

        int sel[100];
        dlx_search(m, 0, sel);
        dlx_matrix_delete(m);
    }

    fclose(fp);

    return 0;
}
